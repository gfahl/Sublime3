import sublime, sublime_plugin, User.sublime_util as su
import re

class CopyFilenameCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        s = self.view.file_name()
        sublime.set_clipboard(re.match('.*[/\\\\](.*)', s).group(1))
        sublime.status_message("Copied file name")

    def is_enabled(self):
        s = self.view.file_name()
        return not(not(s and len(s) > 0))
