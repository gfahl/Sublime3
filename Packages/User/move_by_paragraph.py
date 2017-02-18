import sublime, sublime_plugin, User.sublime_util as su

class MoveByParagraphCommand(sublime_plugin.TextCommand):
    def run(self, edit, extend = False, forward = True):
        v = self.view
        new_sel = []
        any_new_b_visible = False
        fallback_center_pt = None

        for rg in v.sel():
            old_a = rg.a
            old_b = rg.b
            pt = v.line(old_b).begin() # to mimic TextPad's behaviour
            if forward:
                _rg = v.find("\n\s*\n", pt)
                new_b = _rg.b if _rg else v.size()
            else:
                _rg = v.find_prev("\n\s*\n", pt)
                new_b = _rg.b if _rg else 0
            if v.visible_region().contains(old_b):
                fallback_center_pt = new_b
            any_new_b_visible = any_new_b_visible or v.visible_region().contains(new_b)
            new_a = old_a if extend else new_b
            new_sel.append(sublime.Region(new_a, new_b))
        v.set_selection(new_sel)
        if not any_new_b_visible and fallback_center_pt != None:
            v.show_at_center(fallback_center_pt)
