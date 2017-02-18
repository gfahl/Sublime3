import sublime, sublime_plugin, User.sublime_util as su

class ExtendMultiselectionCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward):
        v = self.view
        rg = v.sel()[-1 if forward else 0]
        new_row = v.row(rg.a) + (1 if forward else -1)
        a = v.text_point(new_row, v.col(rg.a))
        b = v.text_point(new_row, v.col(rg.b))
        v.sel().add(sublime.Region(a, b))
