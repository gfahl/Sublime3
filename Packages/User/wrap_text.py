import sublime, sublime_plugin, User.sublime_util as su
import uuid

class WrapTextCommand(sublime_plugin.TextCommand):
    def run(self, edit, width = None):
        s = '\n\n' + str(uuid.uuid4()) + '\n\n'
        v = self.view
        for rg in v.sel():
            v.replace(edit, rg, v.substr(rg).replace('\n', s))
        if width == None:
            v.run_command('wrap_lines')
        else:
            v.run_command('wrap_lines', {'width': width})
        for rg in v.sel():
            v.replace(edit, rg, v.substr(rg).replace(s, '\n'))
