import sublime, sublime_plugin, User.sublime_util as su
import re

class SqueezeWhitespaceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view
        for region in v.sel():
            old_text = v.substr(region)
            regex = re.compile('\s{2,}', flags=re.MULTILINE)
            new_text = re.sub(regex, ' ', old_text)
            v.replace(edit, region, new_text)
