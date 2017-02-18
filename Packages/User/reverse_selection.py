import sublime, sublime_plugin, User.sublime_util as su

class ReverseSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view
        new_sel = []
        for s in v.sel():
            new_sel.append(sublime.Region(s.b, s.a))
        v.set_selection(new_sel)
