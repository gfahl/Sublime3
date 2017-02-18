import sublime, sublime_plugin, User.sublime_util as su

class PromptMoveUsingFindCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel("Find:", "", self.on_done, None, None)

    def on_done(self, text):
        self.window.active_view().run_command("move_using_find", {"regex": text} )

class MoveUsingFindCommand(sublime_plugin.TextCommand):

    def run(self, edit, regex):
        v = self.view
        new_sel = []
        for rg in v.sel():
            new_rg = v.find(regex, rg.a)
            new_sel.append(new_rg)
        v.set_selection(new_sel)
