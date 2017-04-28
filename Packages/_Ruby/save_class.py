import sublime, sublime_plugin, sublime_util as su
import re, string

class SaveClassCommand(sublime_plugin.WindowCommand):

    def run(self):
        v = self.window.active_view()
        m = re.search('^\s*class\s+(\w+)', v.substr(sublime.Region(0, v.size())), re.MULTILINE)
        if m:
            s = m.group(1)
            buffer_name = "_".join(map(string.lower, re.findall("[A-Z][a-z]*", s))) + ".rb"
            v.set_name(buffer_name)
            v.run_command('prompt_save_as');
        else:
            sublime.status_message("Could not find class name")
