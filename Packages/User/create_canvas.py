import sublime, sublime_plugin, User.sublime_util as su

class CreateCanvasCommand(sublime_plugin.TextCommand):
    # Empty selections: inserts HEIGHT rows of WIDTH spaces
    # Non-empty selections: make each row WIDTH chars long by right-padding spaces
    def run(self, edit):
        HEIGHT = 20
        WIDTH = 200
        v = self.view
        new_sel = []
        for r in reversed(v.sel()):
            if r.empty():
                new_text = (" " * WIDTH + "\n") * HEIGHT
                n = len(new_text)
                _new_sel = []
                for rg in reversed(new_sel):
                    _new_sel.append(sublime.Region(rg.a + n, rg.b + n))
                new_sel = _new_sel
                v.insert(edit, r.a, new_text)
                new_sel.append(sublime.Region(r.a, r.a + n))
            else:
                lines = v.lines(r)
                old_a = lines[0].a
                old_b = lines[-1].b
                region = sublime.Region(old_a, old_b)
                new_lines = []
                for line in lines:
                    new_lines.append(v.substr(line) + " " * (WIDTH - line.size()))
                new_text = "\n".join(new_lines)
                new_b = old_a + len(new_text)
                n = new_b - old_b
                _new_sel = []
                for rg in reversed(new_sel):
                    _new_sel.append(sublime.Region(rg.a + n, rg.b + n))
                new_sel = _new_sel
                v.replace(edit, region, new_text)
                new_sel.append(sublime.Region(old_a, new_b + 1))
        v.set_selection(new_sel)
        v.settings().set('draw_white_space', 'all')
