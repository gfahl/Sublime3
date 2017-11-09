import sublime, sublime_plugin, User.sublime_util as su
import difflib, time, os

class DiffPreviousCommand(sublime_plugin.WindowCommand):
    def run(self):
        win = self.window

        win.run_command("next_view_in_stack")
        v = win.active_view()
        txt1 = v.substr(sublime.Region(0, v.size())).splitlines()
        name1 = v.file_name()
        date1 = time.ctime(os.stat(name1).st_mtime)

        win.run_command("prev_view_in_stack")
        v = win.active_view()
        txt2 = v.substr(sublime.Region(0, v.size())).splitlines()
        name2 = v.file_name()
        date2 = time.ctime(os.stat(name2).st_mtime)

        diff = difflib.unified_diff(txt1, txt2, name1, name2, date1, date2, lineterm = '')
        difftxt = u"\n".join(line for line in diff)
        if len(difftxt) == 0:
            difftxt = "--- " + name1 + " " + date1 + "\n"
            difftxt += "+++ " + name2 + " " + date2 + "\n"
            difftxt += "@@ (the files are identical) @@\n"

        try:
            v = next(_v for _v in win.views() if _v.is_scratch() and _v.name() == u'Diff')
            win.focus_view(v)
        except StopIteration:
            v = win.new_file()
            v.set_name("Diff")
            v.set_scratch(True)
            v.set_syntax_file('Packages/Diff/Diff.tmLanguage')

        pt = v.size()
        v.run_command('append', {'characters': "\n" + difftxt + "\n"})
        v.set_selection([sublime.Region(pt + 1, pt + 1)])
        v.set_viewport_position((v.viewport_position()[0], v.layout_extent()[1]))
        v.show(pt, False)
