import sublime, sublime_plugin, User.sublime_util as su
import re

class ShowPropertiesCommand(sublime_plugin.WindowCommand):
    def run(self):
        w = self.window
        v = w.active_view()
        props = [] # key-value pairs
        if v.file_name():
            m = re.match('(.*)[/\\\\](.*)', v.file_name())
            props.append(["Filename", m.group(2)])
            props.append(["Directory", m.group(1)])
        else:
            props << ["Filename", "n/a"] << ["Directory", "n/a"]
        props.append(["Encoding", v.encoding()])
        props.append(["Tab Width", v.settings().get('tab_size')])
        props.append(["Indentation", "Spaces" if v.settings().get('translate_tabs_to_spaces') else "Tabs"])
        props.append(["Size", "%d characters" % v.size()])
        props.append(["Selection", list(v.sel())])
        props.append(["Line Endings", v.line_endings()])
        props.append(["Syntax File", v.settings().get('syntax')])
        props.append(["Scope at point", v.scope_name(v.sel()[0].a) if v.empty_selection() else "n/a"])
        props.append(["Color Scheme", v.settings().get('color_scheme')])
        props.append(["Font", "%s %dpt" % (v.settings().get('font_face'), v.settings().get('font_size'))])
        panel = self.window.create_output_panel('properties')
        panel.run_command("append", {"characters": "-Properties\n"})
        for prop in props:
            panel.run_command("append", {"characters": "\n_%s_ %s" % (prop[0], prop[1])})
        panel.set_syntax_file("Packages/GText/GText.sublime-syntax")
        self.window.run_command('show_panel', {'panel':'output.properties'})
