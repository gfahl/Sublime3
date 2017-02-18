import sublime, sublime_plugin, User.sublime_util as su

class EncloseInQuotesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        _enclose("quotes", self.view, edit)

class InsertQuotesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        _insert("quotes", self.view, edit)

class EncloseInParenthesesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        _enclose("parentheses", self.view, edit)

class InsertParenthesesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        _insert("parentheses", self.view, edit)

def _enclose(_type, v, edit):
    if any(rg.empty() for rg in v.sel()):
        v.window().run_command("find_under_expand")
    a = sublime.load_settings("Preferences.sublime-settings").get(_type)
    for rg in v.sel():
        if rg.empty(): continue
        s = v.substr(rg)
        curr = s[0] + s[-1]
        ix = a.index(curr) if curr in a else None
        if ix == None:
            new_s = a[0][0] + s + a[0][1]
        elif ix == len(a) - 1:
            new_s = s[1:-1]
        else:
            new_s = a[ix + 1][0] + s[1:-1] + a[ix + 1][1]
        v.replace(edit, rg, new_s)

def _insert(_type, v, edit):
    a = sublime.load_settings("Preferences.sublime-settings").get(_type)
    new_sel = []
    for rg in v.sel():
        if not rg.empty():
            new_sel.append(rg)
            continue
        curr = v.substr(sublime.Region(rg.a - 1, rg.a + 1))
        ix = a.index(curr) if curr in a else None
        if ix == None:
            v.replace(edit, sublime.Region(rg.a, rg.a), a[0])
            new_sel.append(sublime.Region(rg.a + 1, rg.a + 1))
        elif ix == len(a) - 1:
            v.replace(edit, sublime.Region(rg.a - 1, rg.a + 1), "")
            new_sel.append(sublime.Region(rg.a - 1, rg.a - 1))
        else:
            v.replace(edit, sublime.Region(rg.a - 1, rg.a + 1), a[ix + 1])
            new_sel.append(sublime.Region(rg.a, rg.a))
    v.set_selection(new_sel)
