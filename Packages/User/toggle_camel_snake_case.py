import sublime, sublime_plugin, User.sublime_util as su
import re

class ToggleCamelSnakeCaseCommand(sublime_plugin.TextCommand):
    # changes selection as follows:
    # "foo fie fum" => "foo_fie_fum" => "FooFieFum" => "foo fie fum" etc.
    def run(self, edit):
        v = self.view
        for rg in v.sel():
            s = v.substr(rg)
            if s.find("_") >= 0:
                s = "".join([x.capitalize() for x in s.split("_")])
            elif s.find(" ") >= 0:
                s = s.replace(" ", "_")
            else:
                s = s[0].upper() + s[1:] # make fooFieFum behave like FooFieFum
                s = " ".join([x.lower() for x in re.findall("[A-Z][a-z]*", s)])
            v.replace(edit, rg, s)
