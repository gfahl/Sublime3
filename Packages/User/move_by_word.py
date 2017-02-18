import sublime, sublime_plugin, User.sublime_util as su
import re

class MoveByWordCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward = True, extend = False):
        delta = 1 if forward else -1
        v = self.view
        new_sel = []
        show_point = None

        for rg in v.sel():
            old_a = rg.a
            old_b = rg.b
            line_extremity = v.line(old_b).end() if forward else v.line(old_b).begin()
            if old_b == line_extremity:
                new_b = old_b + delta
            else:
                s = v.substr(sublime.Region(old_b, line_extremity))[::delta]
                m = re.search(r'(\S\s|\w\W|[^\s\w]\w)', s, re.UNICODE)
                new_b = old_b + (m.start() + 1) * delta if m else line_extremity
            new_a = old_a if extend else new_b
            new_sel.append(sublime.Region(new_a, new_b))
            if v.visible_region().contains(old_b):
                show_point = new_b
        v.set_selection(new_sel)
        if show_point == None:
            show_point = new_sel[0].b
        v.show(show_point)
