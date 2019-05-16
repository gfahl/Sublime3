import sublime, sublime_plugin, User.sublime_util as su
import math

class CenterTextCommand(sublime_plugin.TextCommand):
    # Example: selected text "      Foo Fie Fum" becomes "   Foo Fie Fum   "
    def run(self, edit):
        v = self.view
        for rg in v.sel():
            s = v.substr(rg)
            s2 = s.strip()
            no_of_spaces = len(s) - len(s2)
            s1 = " " * math.floor(no_of_spaces / 2)
            s3 = " " * math.ceil(no_of_spaces / 2)
            v.replace(edit, rg, s1 + s2 + s3)
