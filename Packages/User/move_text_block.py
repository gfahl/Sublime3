import sublime, sublime_plugin, User.sublime_util as su

def move_text_horizontally(v, edit, delta):
    for rg in v.sel():
        v.sel().subtract(rg)
        s = v.substr(rg)
        v.erase(edit, rg)
        v.insert(edit, rg.begin() + delta, s)
        v.sel().add(sublime.Region(rg.a + delta, rg.b + delta))

def move_text_vertically(v, edit, delta):
    new_sel = []
    for rg in list(v.sel())[::-delta]:
        text = v.substr(rg)
        rc1 = v.rowcol(rg.begin())
        rc2 = v.rowcol(rg.end())
        p1 = v.text_point(rc1[0] + delta, rc1[1])
        p2 = v.text_point(rc2[0] + delta, rc2[1])
        new_region = sublime.Region(p1, p2)
        s = v.substr(new_region)
        v.replace(edit, new_region, text)
        v.replace(edit, rg, s)
        new_sel.append(new_region)
    v.set_selection(new_sel)

class MoveTextBlockCommand(sublime_plugin.TextCommand):
    def run(self, edit, horizontally, forward):
        delta = 1 if forward else -1
        if horizontally:
            move_text_horizontally(self.view, edit, delta)
        else:
            move_text_vertically(self.view, edit, delta)
