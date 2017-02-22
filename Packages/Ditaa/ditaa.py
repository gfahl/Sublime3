import sublime, sublime_plugin, User.sublime_util as su
import random, re, string

class DitaaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        jar = sublime.load_settings("Ditaa.sublime-settings").get("ditaa_jar")
        self.ditaa_cmd = 'java -jar "%s/Ditaa/%s"' % (sublime.packages_path(), jar)
        self.cmd_separator = ' & ' if sublime.platform() == 'windows' else '; '
        self.delete_cmd = 'del' if sublime.platform() == 'windows' else 'rm'
        remaining = self.get_ditaa_data(self.view)
        if remaining:
            input_filename = remaining[-1][0]
            v = self.view.window().open_file(input_filename)
            self.process_patiently(v, remaining, [])

    def get_ditaa_data(self, v):
        comment_regions = v.find_by_selector("comment")
        comment_def_regions = v.find_by_selector("punctuation.definition.comment")
        res = []
        regex1 = re.compile('^\s*ditaa(.?) (.*)', re.MULTILINE | re.DOTALL)
        regex2 = re.compile('([^\n]*)\n(.*)', re.MULTILINE | re.DOTALL)
        for rg in comment_regions:
            s = v.substr(rg)
            for _rg in reversed(comment_def_regions):
                if _rg.a >= rg.a and _rg.a <= rg.b:
                    s = s[:_rg.a - rg.a] + s[_rg.b - rg.a:]
            m = regex1.search(s)
            if m:
                swap_char, rest = m.group(1, 2)
                if swap_char:
                    # necessary since "--" is illegal within html comments
                    rest = ''.join([
                        swap_char if c == '-' else '-' if c == swap_char else c
                        for c in list(rest)
                        ])
                m = regex2.match(rest)
                args, dia = m.group(1, 2)
                random_str = ''.join([random.choice(string.ascii_letters) for _ in range(8)])
                inpfile = 'ditaa_%s.tmp' % random_str
                res.append([inpfile, args, dia])
        return res

    def process_patiently(self, v, remaining, commands):
        if v.is_loading():
            sublime.set_timeout(lambda: self.process_patiently(v, remaining, commands), 10)
        else:
            win = v.window()
            inpfile, args, dia = remaining.pop()
            v.run_command("append", {'characters': dia})
            v.run_command("save")
            win.run_command("close")
            commands.append("%s %s %s%s%s %s" % (
                self.ditaa_cmd, inpfile, args,
                self.cmd_separator,
                self.delete_cmd, inpfile))
            if remaining:
                input_filename = remaining[-1][0]
                v = self.view.window().open_file(input_filename)
                self.process_patiently(v, remaining, commands)
            else:
                win.run_command("exec", args = { "shell_cmd": self.cmd_separator.join(commands) })
