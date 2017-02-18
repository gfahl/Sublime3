import sublime, sublime_plugin, User.sublime_util as su
import re

class ShowPropertiesCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.active_view()
        s = ""
        if v.file_name():
            m = re.match('(.*)[/\\\\](.*)', v.file_name())
            s += "Filename: %s\n" % m.group(2)
            s += "Directory: %s\n" % m.group(1)
        else:
            s += "Filename: n/a\n"
            s += "Directory: n/a\n"
        s += "Encoding: %s\n" % v.encoding()
        s += "Tab Width: %s\n" % v.settings().get('tab_size')
        s += "Indentation: %s\n" % ("Spaces" if v.settings().get('translate_tabs_to_spaces') else "Tabs")
        s += "Size: %d characters\n" % v.size()
        s += "Selection: %s\n" % list(v.sel())
        s += "Line Endings: %s\n" % v.line_endings()
        s += "Syntax File: %s\n" % v.settings().get('syntax')
        if v.empty_selection():
            s += "Scope at point: %s\n" % v.scope_name(v.sel()[0].a)
        else:
            s += "Scope at point: n/a\n"
        s += "Color Scheme: %s\n" % v.settings().get('color_scheme')
        s += "Font: %s %dpt\n" % (v.settings().get('font_face'), v.settings().get('font_size'))
        sublime.message_dialog(s)
        print(s)
