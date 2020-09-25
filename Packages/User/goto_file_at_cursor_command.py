import sublime, sublime_plugin, User.sublime_util as su

class GotoFileAtCursorCommand(sublime_plugin.WindowCommand):
    def run(self):
        win = self.window
        v = win.active_view()
        rg = v.sel()[0]
        if rg.empty():
            win.run_command("find_under_expand")
            rg = v.sel()[0]
        s = v.substr(rg)
        self.window.run_command("show_overlay", {"overlay": "goto", "text": s})
