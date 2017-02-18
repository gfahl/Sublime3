import sublime, sublime_plugin, User.sublime_util as su

class RightPadSpacesCommand(sublime_plugin.TextCommand):
    # Add spaces to make lines equally long
    #     these are>           these are   >
    #     some example>   =>   some example>
    #     lines>               lines       >
    # A selection may start and/or end in the middle of a row
    def run(self, edit):
        new_sel = []
        for selection in reversed(self.view.sel()):
            lines = self.view.lines(selection)
            old_a = lines[0].a
            old_b = lines[-1].b
            region = sublime.Region(old_a, old_b)
            max_len = max(map(lambda line: line.b - line.a, lines))
            new_lines = []
            for line in lines:
                new_lines.append(self.view.substr(line) + " " * (max_len - line.size()))
            new_text = "\n".join(new_lines)
            new_b = old_a + len(new_text)
            _new_sel = []
            n = new_b - old_b
            for rg in reversed(new_sel):
                _new_sel.append(sublime.Region(rg.a + n, rg.b + n))
            new_sel = _new_sel
            new_sel.append(sublime.Region(old_a, new_b + 1))
            self.view.replace(edit, region, new_text)
        self.view.set_selection(new_sel)
