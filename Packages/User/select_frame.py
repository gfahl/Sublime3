import sublime, sublime_plugin, User.sublime_util as su
import time

class SelectFrameCommand(sublime_plugin.TextCommand):
    def __init__(self, v):
        sublime_plugin.TextCommand.__init__(self, v)
        self.last_invocation_time = 0

    def run(self, edit):
        v = self.view

        now = time.time()
        elapsed_time = now - self.last_invocation_time
        self.last_invocation_time = now

        if v.command_history(0)[0] == 'select_frame' or elapsed_time < 1:
            # Sublime's command history doesn't immediately record a new command
            # Unless we look at elapsed time too, rapid consecutive calls do not work
            self.ix += 1
        else:
            self.original_selection = [rg for rg in v.sel()]
            #
            v.sel().clear()
            for rg in self.original_selection:
                # make sure correct frame is selected when selection width = 0
                v.sel().add(sublime.Region(rg.a - 1, rg.a + 1) if rg.empty() else rg)
            #
            self.found_frames = []
                # used for avoiding recursion down branches that have already been tried
            self.get_frames(su.Rect.from_selection(v))
            self.found_frames = list(filter(lambda f: f.height() >= 3 and f.width() >= 3, self.found_frames))
            self.found_frames.sort(key = lambda x: x.size())
            self.ix = 0

        if self.ix == len(self.found_frames):
            v.set_selection(self.original_selection)
            sublime.status_message(
                "no frames found" if self.found_frames == [] else "original selection")
            self.ix = -1
        else:
            self.found_frames[self.ix].use_as_selection()
            sublime.status_message("frame %d of %d" % (self.ix + 1, len(self.found_frames)))

    def frame_already_found(self, cand):
        return next((f for f in self.found_frames if f.pos_as_tuple() == cand.pos_as_tuple()), None)

    def get_frames(self, rect):
        # returns all frames which contain <rect> and are bigger than <rect>
        return (
            self.get_frames0(rect.copy().expand('W')) +
            self.get_frames0(rect.copy().expand('N')) +
            self.get_frames0(rect.copy().expand('E')) +
            self.get_frames0(rect.copy().expand('S'))
            )

    def get_frames0(self, rect):
        # returns all frames which contain <rect> and are bigger than or equal to <rect>
        if not rect.is_valid(): return []

        failure = False
        direction_queue = list(su.Rect.directions)
        while not failure and not rect.is_frame():
            search_direction = direction_queue[0]
            direction_queue = direction_queue[1:] + direction_queue[:1]
            while rect.is_valid() and not rect.is_line(search_direction):
                rect.expand(search_direction)
            failure = not rect.is_line(search_direction)

        if rect.is_frame() and not self.frame_already_found(rect):
            self.found_frames.append(rect)
            return [rect] + self.get_frames(rect)
        else: return []
