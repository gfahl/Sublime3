import sublime, sublime_plugin, User.sublime_util as su

class NextWordExpandCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        v = self.view
        last_rg = v.sel()[-1]
        rg = v.find('\w+', last_rg.end())
        if rg:
            rg = v.word(rg) # in case last cursor was in the middle of a word
            new_sel = [r for r in v.sel()]
            if last_rg.intersects(rg) or last_rg.empty():
                new_sel = new_sel[:-1]
            new_sel.append(rg)
            v.set_selection(new_sel)

class NextWordExpandSkipCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        v = self.view
        last_rg = v.sel()[-1]
        new_sel = [r for r in v.sel()][:-1] + [sublime.Region(last_rg.end(), last_rg.end())]
        v.set_selection(new_sel)
        v.run_command('next_word_expand')
