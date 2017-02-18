import sublime, sublime_plugin, User.sublime_util as su

def get_preference(key):
    if key == "font_factor_japanese":
        f = "Preferences.sublime-settings"
    elif sublime.platform() == "windows":
        f = "Preferences (Windows).sublime-settings"
    elif sublime.platform() == "osx":
        f = "Preferences (OSX).sublime-settings"
    else:
        f = "Preferences (Linux).sublime-settings"
    s = sublime.load_settings(f)
    return s.get(key)

def set_font(v, face, sz):
    s = v.settings()
    if face:
        s.set("font_face", face)
    if sz:
        s.set("font_size", sz)
    sublime.status_message("Font: %s %dpt" % (s.get("font_face"), s.get("font_size")))

class ChangeFontSizeCommand(sublime_plugin.TextCommand):
    def run(self, edit, increase = True):
        v = self.view
        current_size = v.settings().get("font_size")
        sizes = get_preference("font_sizes")
        if sizes:
            if increase:
                new_size = next((size for size in sizes if size > current_size), sizes[-1])
            else:
                new_size = next((size for size in reversed(sizes) if size < current_size), sizes[0])
            set_font(v, None, new_size)

class ResetFontCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view
        new_size = get_preference("font_size")
        if v.score_selector(0, "text.japanese") > 0:
            new_size *= get_preference("font_factor_japanese")
            new_face = get_preference("font_face_japanese")
        else:
            new_face = get_preference("font_face")
        set_font(v, new_face, new_size)

class FontEventListener(sublime_plugin.EventListener):
    def main(self, view):
        if view.settings().get('is_widget'): return
        if view.settings().get("font_initialized"): return
        view.run_command('reset_font')
        view.settings().set("font_initialized", True)

    def on_activated(self, view):
        self.main(view)

    def on_load(self, view):
        self.main(view)

    def on_new(self, view):
        self.main(view)
