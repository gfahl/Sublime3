import sublime, sublime_plugin, sublime_util as su
import re

class ConvertBlockCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for rg in self.view.sel():
            s = self.view.substr(rg)
            m = re.match('{\s*(\|.*?\|)?\s*(.*?)\s*}$', s, re.DOTALL)
            if m:
                new_s = "do"
                if m.group(1):
                    new_s += " " + m.group(1)
                new_s += "\n" + m.group(2) + "\nend"
                self.view.replace(edit, rg, new_s)
            m = re.match('do\s*(\|.*?\|)?\s*(.*?)\s*end$', s, re.DOTALL)
            if m:
                new_s = "{ "
                if m.group(1):
                    new_s += m.group(1) + " "
                new_s += m.group(2) + " }"
                self.view.replace(edit, rg, new_s)
        self.view.run_command('reindent', {'force_indent': False})
