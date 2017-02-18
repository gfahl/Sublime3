import sublime, sublime_plugin, User.sublime_util as su

class TrimTrailingWhiteSpaceNow(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = self.view.find_all("[\t ]+$")
        for r in reversed(regions):
            self.view.erase(edit, r)
