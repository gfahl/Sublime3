import sublime, sublime_plugin, User.sublime_util as su
import re

def get_command_name(v, fallback_python_command_name):
    python_command_name = fallback_python_command_name
    syntax_file = v.settings().get('syntax')
    m = re.match('.*/([ \w]+)\.(?:tmLanguage|sublime\-syntax)$', syntax_file)
    if m:
        syntax_name = m.group(1).replace(' ', '')
        cand = re.sub('Command$', syntax_name + 'Command', python_command_name)
        text_commands = sublime_plugin.all_command_classes[2]
        cmd = next((cmd for cmd in text_commands if cmd.__name__.lower() == cand.lower()), None)
        if cmd:
            python_command_name = cmd.__name__
        else:
            pass # no syntax specific command
    else:
        pass # no syntax identified
    return su.to_snake_case(re.sub('Command$', '', python_command_name))

class FoldByLevelDispatchCommand(sublime_plugin.TextCommand):
    def run(self, edit, level):
        self.view.run_command(get_command_name(self.view, 'FoldByLevelCommand'), { 'level': level })

class FoldDispatchCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command(get_command_name(self.view, 'FoldCommand'))

class UnfoldAllDispatchCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command(get_command_name(self.view, 'UnfoldAllCommand'))

class UnfoldDispatchCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command(get_command_name(self.view, 'UnfoldCommand'))
