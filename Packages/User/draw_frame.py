import sublime, sublime_plugin, User.sublime_util as su

class DrawFrameCommand(sublime_plugin.TextCommand):
    # Draws an ascii frame
    def run(self, edit, vertical = '|'):
        v = self.view
        sel = v.sel()
        if len(sel) == 1 and v.line(sel[0].a) != v.line(sel[0].b):
            # Add one line above & below, and two 'columns' left & right; then draw the frame
            #
            # <BOL>abc <suppose          <BOL>+-----------------+
            # <BOL>this text was     =>  <BOL>| abc suppose     |
            # <BOL>selected> ghijkl      <BOL>| this text was   |
            #                            <BOL>| selected ghijkl |
            #                            <BOL>+-----------------+
            p1 = v.line(sel[0].begin()).a
            v.insert(edit, p1, '\n')
            p2 = v.line(sel[0].end() - 1).b
            v.insert(edit, p2, '\n')
            v.set_selection([sublime.Region(p1, p2 + 2)])
            self.view.run_command('right_pad_spaces')
            v.set_selection(v.lines(sel[0]))
            for rg in sel:
                v.replace(edit, rg, '  ' + v.substr(rg) + '  ')
            su.Rect.from_selection(v).draw_frame(edit, vertical)
            v.set_selection([sublime.Region(sel[0].a, sel[-1].b + 1)])
        elif v.sel().is_rectangular(v):
            # <BOL>abc <suppose      > jkl       <BOL>abc +-----------+ jkl
            # <BOL>def <this text was> mno   =>  <BOL>def |his text wa| mno
            # <BOL>ghi <selected     > pqr       <BOL>ghi +-----------+ pqr
            su.Rect.from_selection(v).draw_frame(edit, vertical)
