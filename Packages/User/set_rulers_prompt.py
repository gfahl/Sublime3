import sublime, sublime_plugin, User.sublime_util as su

class SetRulersPromptCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Rulers:", "", self.on_done, None, None)

    def on_done(self, text):
        columns = [int(s) for s in text.split(',') if s.strip().isdigit()]
        self.window.active_view().settings().set('rulers', columns)
