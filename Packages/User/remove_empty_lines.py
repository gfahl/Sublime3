import sublime, sublime_plugin, User.sublime_util as su
import re

class RemoveEmptyLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        new_sel = []
        for region in self.view.sel():
            old_text = self.view.substr(region)
            regex = re.compile('^\s*$\n', flags=re.MULTILINE)
            new_text = re.sub(regex, '', old_text)
            self.view.replace(edit, region, new_text)
