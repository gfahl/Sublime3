import sublime, sublime_plugin, User.sublime_util as su
import re

def n_to_col(n):
    quotient, remainder = divmod(n - 1, 26)
    return '' if n == 0 else n_to_col(quotient) + chr(ord('a') + remainder)

def col_to_n(col):
    return 0 if col == '' else col_to_n(col[:-1]) * 26 + ord(col[-1]) - ord('a') + 1

class PasteEnumerationCommand(sublime_plugin.TextCommand):
    def run(self, edit, start = '1'):
        v = self.view
        regions = v.sel()
        if re.match('[0-9]+$', start):
            n = int(start)
            for rg in regions:
                v.replace(edit, rg, str(n))
                n += 1
        elif re.match('[a-z]+$', start):
            n = col_to_n(start)
            for rg in regions:
                v.replace(edit, rg, n_to_col(n))
                n += 1

class PasteEnumerationPromptCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Start:", "", self.on_done, None, None)

    def on_done(self, text):
        self.window.active_view().run_command("paste_enumeration", {"start": text} )
