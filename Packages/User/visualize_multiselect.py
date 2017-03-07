import sublime, sublime_plugin, User.sublime_util as su

class VisualizeMultiselectEventListener(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        if len(view.sel()) > 1:
            view.settings().set('caret_extra_width', 2)
        else:
            view.settings().erase('caret_extra_width')
