import sublime, sublime_plugin, User.sublime_util as su
import re

class SqueezeEmptyLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view
        for region in v.sel():
            old_text = v.substr(region)
            regex = re.compile('\n[\n\s]*\n', flags=re.MULTILINE)
            new_text = re.sub(regex, '\n\n', old_text)
            if v.substr(region.begin() - 1) == '\n' and new_text[0:2] == '\n\n':
                new_text = new_text[1:]
            v.replace(edit, region, new_text)
