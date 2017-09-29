import sublime, sublime_plugin, User.sublime_util as su

class ScrollHorizontallyCommand(sublime_plugin.TextCommand):
    def run(self, edit, amount):
        v = self.view
        x, y = v.viewport_position()
        x += amount * v.em_width()
        x = min(max(x, 0), v.layout_extent()[0] - v.viewport_extent()[0])
        v.set_viewport_position((x, y))
