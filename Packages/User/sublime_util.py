import sublime, re

def col(self, text_point):
    return self.rowcol(text_point)[1]

def empty_selection(self):
    return len(self.sel()) == 1 and self.sel()[0].empty()

def find_prev(self, pattern, from_position):
    rgs = self.find_all(pattern)
    return next((rg for rg in reversed(rgs) if rg.b < from_position), None)

def row(self, text_point):
    return self.rowcol(text_point)[0]

def rowcol_exists(self, row, col):
    return self.rowcol(self.text_point(row, col)) == (row, col)

def set_selection(self, regions):
    self.sel().clear()
    for rg in regions:
        self.sel().add(rg)

sublime.View.col = col
sublime.View.empty_selection = empty_selection
sublime.View.find_prev = find_prev
sublime.View.row = row
sublime.View.rowcol_exists = rowcol_exists
sublime.View.set_selection = set_selection

def is_rectangular(self, v):
    if len(set([(v.col(rg.begin()), v.col(rg.end())) for rg in self])) != 1:
        # start columns, and end columns, have to be equal
        return False
    if v.col(self[0].begin()) == v.col(self[0].end()):
        # width must be >= 1
        return False
    if list(set([v.row(rg.end()) - v.row(rg.begin()) for rg in self])) != [0]:
        # no region can span more than one row
        return False
    if list(range(v.row(self[0].begin()), v.row(self[-1].begin()) + 1, 1)) != [v.row(rg.begin()) for rg in self]:
        # rows should be consecutive
        return False
    return True

sublime.Selection.is_rectangular = is_rectangular

def to_snake_case(s):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

class Rect:
    directions = tuple('WNES')

    @classmethod
    def from_selection(klass, v):
        left = min(map(lambda rg: v.col(rg.begin()), v.sel()))
        top = v.row(v.sel()[0].begin())
        right = max(map(lambda rg: v.col(rg.end()), v.sel()))
        bottom = v.row(v.sel()[-1].end())
        return klass(v, (left, top, right, bottom))

    def __init__(self, v, pos_as_tuple):
        self.v = v
        self.pos = {
            'W': pos_as_tuple[0],
            'N': pos_as_tuple[1],
            'E': pos_as_tuple[2],
            'S': pos_as_tuple[3]
            }

    def __str__(self):
        return "<Rect: (%d, %d) (%d, %d)>" % (self.pos_as_tuple())

    def copy(self):
        return Rect(self.v, self.pos_as_tuple())

    def draw_frame(self, edit, vertical):
        for row in range(self.pos['N'], self.pos['S'] + 1):
            tp1 = self.v.text_point(row, self.pos['W'])
            tp2 = self.v.text_point(row, self.pos['E'])
            rg = sublime.Region(tp1, tp2)
            old_text = self.v.substr(rg)
            if row in (self.pos['N'], self.pos['S']):
                new_text = '+' + re.sub('\\' + vertical, '+', old_text[1:-1])
                new_text = re.sub('[^+]', '-', new_text)
                if self.width() > 1:
                    new_text += '+'
            else:
                new_text = '+' if old_text[0] in '-+' else vertical
                new_text += old_text[1:-1]
                if self.width() > 1:
                    new_text += '+' if old_text[-1] in '-+' else vertical
            self.v.replace(edit, rg, new_text)
        self.use_as_selection()

    def expand(self, direction):
        if direction not in Rect.directions:
            raise Exception('Unexpected direction: %s' % direction)
        delta = -1 if direction == 'W' or direction == 'N' else 1
        self.pos[direction] += delta
        return self

    def height(self):
        return self.pos['S'] - self.pos['N'] + 1

    def is_frame(self):
        return (
            self.is_line('W') and
            self.is_line('N') and
            self.is_line('E') and
            self.is_line('S')
            )

    def is_horizontal_line(self, row, left_col, right_col):
        s = ''
        col = left_col
        while col <= right_col:
            s += self.v.substr(self.v.text_point(row, col))
            col += 1
        return re.match('[+-]+$', s)

    def is_line(self, side):
        if side == 'W':
            return self.is_vertical_line(self.pos['W'], self.pos['N'], self.pos['S'])
        elif side == 'E':
            return self.is_vertical_line(self.pos['E'] - 1, self.pos['N'], self.pos['S'])
        elif side == 'N':
            return self.is_horizontal_line(self.pos['N'], self.pos['W'], self.pos['E'] - 1)
        elif side == 'S':
            return self.is_horizontal_line(self.pos['S'], self.pos['W'], self.pos['E'] - 1)
        else:
            raise Exception('Unexpected side: %s' % side)

    def is_valid(self):
        return (
            self.v.rowcol_exists(self.pos['N'], self.pos['W']) and
            self.v.rowcol_exists(self.pos['N'], self.pos['E']) and
            self.v.rowcol_exists(self.pos['S'], self.pos['W']) and
            self.v.rowcol_exists(self.pos['S'], self.pos['E'])
            )

    def is_vertical_line(self, col, top_row, bottom_row):
        s = ''
        row = top_row
        while row <= bottom_row:
            s += self.v.substr(self.v.text_point(row, col))
            row += 1
        return re.match('[+|]+$', s)

    def pos_as_tuple(self):
        return (self.pos['W'], self.pos['N'], self.pos['E'], self.pos['S'])

    def size(self):
        return self.height() * self.width()

    def text_point(self, corner):
        if corner == 'NW':
            return self.v.text_point(self.pos['N'], self.pos['W'])
        elif corner == 'NE':
            return self.v.text_point(self.pos['N'], self.pos['E'])
        elif corner == 'SE':
            return self.v.text_point(self.pos['S'], self.pos['E'])
        elif corner == 'SW':
            return self.v.text_point(self.pos['S'], self.pos['W'])
        else:
            raise Exception('Unexpected corner: %s' % side)

    def use_as_selection(self):
        regions = []
        for row in range(self.pos['N'], self.pos['S'] + 1, 1):
            a = self.v.text_point(row, self.pos['W'])
            b = self.v.text_point(row, self.pos['E'])
            regions.append(sublime.Region(a, b))
        self.v.set_selection(regions)

    def width(self):
        return self.pos['E'] - self.pos['W']
