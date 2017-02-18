import sublime, sublime_plugin, User.sublime_util as su

def has_bookmarks(view):
    return len(view.get_regions("bookmarks")) > 1

def has_selected_lines(view):
    return len(view.sel()) == 1 and len(view.lines(view.sel()[0])) > 1

class GetMultipleCursorsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view
        if has_selected_lines(v):
            v.run_command('split_selection_into_lines')
            sublime.status_message("Previous selection split into lines")
        elif has_bookmarks(v):
            v.run_command('select_all_bookmarks')
            sublime.status_message("All bookmarks selected")
        else:
            new_sel = []
            for rg in v.sel():
                if rg.a != rg.b:
                    pos = rg.begin()
                    while pos < rg.end():
                        new_sel.append(sublime.Region(pos, pos + 1))
                        pos = pos + 1
                else:
                    new_sel.append(rg)
            v.sel().clear()
            for rg in new_sel:
                v.sel().add(rg)
            sublime.status_message("Previous selection split into single characters")

    def is_enabled(self):
        return has_bookmarks(self.view) or not self.view.empty_selection()
