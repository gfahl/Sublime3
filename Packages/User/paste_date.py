import sublime, sublime_plugin, User.sublime_util as su
import datetime

class PasteDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for s in self.view.sel():
            self.view.replace(edit, s, str(datetime.date.today()))
