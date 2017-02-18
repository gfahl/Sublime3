import sublime, sublime_plugin, User.sublime_util as su

class MoveTabCommand(sublime_plugin.WindowCommand):
    def run(self, forward = True):
        delta = 1 if forward else -1
        w = self.window
        v = w.active_view()
        group, ix = w.get_view_index(v)
        no_of_views = len(w.views_in_group(group))
        ix += delta
        ix = ix % no_of_views
        w.set_view_index(v, group, ix)
        w.focus_view(v)
