import sublime, sublime_plugin, User.sublime_util as su
import re

class FoldByLevelGtextCommand(sublime_plugin.TextCommand):
    def run(self, edit, level):
        v = self.view
        folds = []
        tp = 0
        if level == 1:
            regex = '[~]'
        elif level == 2:
            regex = '[~=]'
        elif level >= 3:
            regex = '[~=\-]'
        while tp < v.size():
            rg = v.full_line(tp)
            s = v.substr(rg)
            if re.match(regex, s):
                if folds != [] and rg.a == folds[-1].b:
                    folds[-1] = sublime.Region(folds[-1].a, folds[-1].b - 1)
            else:
                if folds != [] and rg.a == folds[-1].b:
                    folds[-1] = sublime.Region(folds[-1].a, rg.b)
                else:
                    folds.append(rg)
            tp = v.full_line(tp).b

        v.run_command('unfold_all')
        v.fold(folds)
        v.show(v.sel())

        sublime.status_message("Folded " + str(len(folds)) + " regions")
