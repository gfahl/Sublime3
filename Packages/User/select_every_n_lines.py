import sublime, sublime_plugin, User.sublime_util as su

class SelectEveryXxLinesPromptCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Interval:", "", self.on_done, None, None)

    def on_done(self, text):
        self.window.active_view().run_command("select_every_xx_lines", {"interval": text} )

class SelectEveryXxLinesCommand(sublime_plugin.TextCommand):

    def run(self, edit, interval):
        v = self.view
        new_sel = []
        for i, rg in enumerate(v.lines(v.sel()[0])):
            if i % int(interval) == 0:
                new_sel.append(sublime.Region(rg.a, rg.a))
        v.sel().clear()
        for rg in new_sel:
            v.sel().add(rg)
