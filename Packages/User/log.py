import sublime, sublime_plugin, User.sublime_util as su

class LogCommand(sublime_plugin.WindowCommand):
    def run(self, log_type = 'commands', on_flag = True):
        if log_type == 'commands':
            sublime.log_commands(on_flag)
        elif log_type == 'input':
            sublime.log_input(on_flag)
        else:
            raise Exception('Unexpected log type: %s' % log_type)
        sublime.status_message(
            "Log for " + log_type.capitalize() + " turned " + ("On" if on_flag else "Off"))
