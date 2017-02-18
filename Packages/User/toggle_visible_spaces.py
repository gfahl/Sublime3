import sublime, sublime_plugin, User.sublime_util as su

class ToggleVisibleSpacesCommand(sublime_plugin.WindowCommand):
    def run(self):
        v = self.window.active_view()
        current_value = v.settings().get('draw_white_space')
        if current_value == "selection":
            new_value = "all"
        else:
            new_value = "selection"
        v.settings().set('draw_white_space', new_value)
