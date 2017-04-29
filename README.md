# Sublime3

My [Sublime Text 3](https://www.sublimetext.com/) configuration.
A [cheat sheet](sublime3_cheatsheet.gtxt) exists.

## Commands

These are the commands I use on a regular basis.
The 'Keyboard shortcut' column shows the Windows shortcut.
For the OSX shortcut, replace any reference to the *alt* key with the *super* key.
"ST3" in the 'Implementation' column means that the command uses out-of-the-box Sublime Text 3 functionality.

### Navigation

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
Move by Character/Line | (cursor keys) | no | no | ST3
Move by Word | ctrl+left/right | no | no | `move_by_word` which is a mix between the Windows and OSX 'Move by Word' functionality. In addition, it recognizes Unicode spaces and punctuation.
Move by Word-part | alt+left/right | no | yes | ST3
Move to Beginning/End of Line | ctrl+q, left/right | yes | yes | use `hardbol` instead of `bol` for Beginning of Line
Move to Beginning/End of File | ctrl+q, up/down | yes | yes | ST3
Move by Paragraph | alt+up/down | yes | yes | `move_by_paragraph` which mimics TextPad's behaviour.
Move by Page | ctrl+comma/period | yes | yes | ST3
Move to Matching Bracket | ctrl+m | no | no | ST3
Move Using Find | (none) | n/a | n/a | `prompt_move_using_find`
Undo Cursor Movement | ctrl+u | no | yes | ST3
Redo Cursor Movement | ctrl+shift+u | no | yes | ST3

### Selection

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
Select by Character/Line | (shift + cursor keys) | no | no | ST3
Select by Word | ctrl+shift+left/right | no | no | see Move by Word
Select by Word-part | alt+shift+left/right | no | yes | ST3
Select to Beginning/End of Line | ctrl+q, shift+left/right | yes | yes | see Move to Beginning/End of Line
Select to Beginning/End of File | ctrl+q, shift+up/down | yes | yes | ST3
Select by Paragraph | alt+shift+up/down | yes | yes | see Move by Paragraph
Select by Page | ctrl+shift+comma/period | yes | yes | ST3
Select All | ctrl+a | no | yes | ST3
Select Word | ctrl+d | no | yes | ST3
Expand Selection to Brackets | ctrl+shift+m | no | no | ST3
Expand Selection to Line | ctrl+l | no | yes | ST3
Reverse Selection Direction | ctrl+q, ctrl+r | yes | yes | `reverse_selection`

### Edit

#### Undo/Redo

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
Undo | ctrl+z | no | yes | ST3
Redo/Repeat | ctrl+y | no | yes | ST3

#### Copy

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
Copy | ctrl+c | no | yes | ST3
Copy Path | ctrl+k, ctrl+p | yes | yes | ST3
Copy Filename | ctrl+k, ctrl+f | yes | yes | `copy_filename`

#### Insert

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
Paste | ctrl+v | no | yes | ST3
Duplicate Selection/Line | ctrl+shift+d | no | yes | ST3
Enclose in Parentheses | ctrl+9 | yes | yes | `enclose_in_parentheses`
Enclose in Quotes | ctrl+8 | yes | yes | `enclose_in_quotes`
Force Insert of Tab | shift+tab | no | no | ST3
Insert Parentheses | ctrl+shift+9 | yes | yes | `insert_parentheses`
Insert Quotes | ctrl+shift+8 | yes | yes | `insert_quotes`
Paste Current Date | ctrl+q, ctrl+d | yes | yes | `paste_date`
Paste Enumeration | (none) | n/a | n/a | `paste_enumeration_prompt`
Paste Incrementing Numbers | (none) | n/a | n/a | `paste_enumeration`

#### Update

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
Indentation: Convert to Tabs/Spaces | (none) | n/a | n/a | ST3
Lower Case | ctrl+k, ctrl+l | no | yes | ST3
Move Lines | ctrl+shift+up/down | no | yes | ST3
Reverse Selections | (none) | n/a | n/a | ST3
Shuffle Selections | (none) | n/a | n/a | ST3
Snake Case & Co | ctrl+k, ctrl+s | yes | yes | `toggle_camel_snake_case`
Sort Selections | (none) | n/a | n/a | ST3
Sort Selections (Case Sensitive) | (none) | n/a | n/a | ST3
Title Case | ctrl+k, ctrl+t | yes | yes | ST3
Toggle Comment | ctrl+j | yes | yes | ST3
Transpose | ctrl+t | no | no | ST3
Unique Selections | (none) | n/a | n/a | ST3
Upper Case | ctrl+k, ctrl+u | no | yes | ST3
Wrap Paragraph (prompt for width) | (none) | n/a | n/a | ST3
Wrap Paragraph at *n* characters | (none) | n/a | n/a | ST3
Wrap Paragraph at Ruler | ctrl+k, ctrl+w | yes | yes | ST3

#### Delete

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
Cut | ctrl+x | no | yes | ST3
Delete | backspace | no | no | ST3
Delete Next Character | ctrl+0 | yes | yes | ST3
Delete Current Line | ctrl+shift+k | no | no | ST3
Delete Rest of Line | ctrl+k, ctrl+k | no | no | ST3
Delete Empty Lines | (none) | n/a | n/a | `remove_empty_lines`
Squeeze Empty Lines | (none) | n/a | n/a | `squeeze_empty_lines`
Squeeze Whitepsace | (none) | n/a | n/a | `squeeze_whitespace`
Trim Trailing Whitespace | (none) | n/a | n/a | `trim_trailing_white_space_now`

### View

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
Scroll Up/Down | ctrl+up/down | no | yes | ST3
Toggle Word Wrap | ctrl+q, ctrl+w | yes | yes | ST3
Toggle Visible Spaces | ctrl+q, ctrl+space | yes | yes | `toggle_visible_spaces`
Decrease Font Size | ctrl+q, ctrl+down | yes | yes | `change_font_size`
Increase Font Size | ctrl+q, ctrl+up | yes | yes | `change_font_size`
Reset Font | ctrl+q, ctrl+left | yes | yes | `reset_font`
Indentation: Tab Width 2 | (none) | n/a | n/a | ST3
Indentation: Tab Width 4 | (none) | n/a | n/a | ST3
Show Properties | (none) | n/a | n/a | `show_properties`

### Search

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
Find | ctrl+f | no | yes | ST3
Find Word Under | alt+f | yes | yes | ST3
Find Previous Word Under | alt+shift+f | yes | yes | ST3
Find in Files | ctrl+shift+f | no | yes | ST3
Next/Previous 'Find in Files' Result | alt+n/p | yes | yes | ST3
Replace | ctrl+h | no | yes | ST3

### File

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
New | ctrl+n | no | yes | ST3
Open | ctrl+o | no | yes | ST3
Save | ctrl+s | no | yes | ST3
Save As… | ctrl+shift+s | no | yes | ST3
Close | ctrl+w | no | yes | ST3
Re-Open Last Closed File | ctrl+shift+t | no | yes | ST3
Switch Tab (Stack Order) | ctrl+tab | no | no | ST3
Switch Tab | alt+comma/period | yes | yes | ST3
Move Tab | alt+shift+comma/period | yes | yes | `move_tab`
Switch to Tab *n* | alt+*n* | no | no | ST3
New Window | ctrl+shift+n | no | yes | ST3
Close Window | ctrl+shift+w | no | yes | ST3

### Multi-Select

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
More | ctrl+d | no | yes | ST3
More But Not This One | ctrl+k, ctrl+d | no | yes | ST3
Next Word | ctrl+e | yes | yes | `next_word_expand`
Next Word But Not This One | ctrl+k, ctrl+e | yes | yes | `next_word_expand_skip`
All Occurances | alt+d | yes | yes | ST3
Get Multiple Cursors | ctrl+shift+l | yes | yes | `get_multiple_cursors`

### Bookmarks

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
Toggle | ctrl+b | yes | yes | ST3
Clear All | ctrl+shift+b | yes | yes | ST3
Next | super+b | yes | yes | ST3
Previous | super+shift+b | yes | yes | ST3

### Canvas

Commands for drawing simple diagrams on a grid of spaces.

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
Create | ctrl+alt+space | yes | yes | `create_canvas`
Draw Frame | ctrl+alt+f | yes | yes | `draw_frame`
Select Frame | ctrl+alt+return | yes | yes | `select_frame`
Extend Selection Up/Down | ctrl+alt+comma/period | yes | yes | `extend_multiselection`
Move Selection | (ctrl + alt + cursor keys) | yes | yes | `move_text_block`

### Tools

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
Goto Anything | ctrl+p | no | yes | ST3
Command Palette | ctrl+shift+c | yes | yes | ST3
Switch Project | ctrl+shift+p | yes | yes | ST3
Show Completions | ctrl+space | no | no | ST3
Toggle Console | ctrl+i | yes | yes | ST3
Toggle Sidebar | ctrl+k, ctrl+b | no | yes | ST3
Focus Sidebar | alt+0 | yes | yes | ST3
Start/End Recording Macro | ctrl+shift+r | yes | yes | ST3
Run Macro | ctrl+r | yes | yes | ST3
Open Containing Folder | ctrl+q, ctrl+e | yes | yes | ST3
Reveal Current File in Sidebar | ctrl+q, ctrl+s | yes | yes | ST3
Diff Previous | (none) | n/a | n/a | `diff_previous`

### Ruby

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
Save Using Snake-Case Version of Class Name | (none) | n/a | n/a | `save_class`
Convert Block Style ({} <-> do...end) | (none) | n/a | n/a | `convert_block`

### Code Folding

Code folding logic has been made syntax dependent. The `<command>_dispatch` commands (e.g. `fold_dispatch`)
look for a subclass to `sublime_plugin.TextCommand` with the name `<Command><Syntax>Command`
(e.g. `FoldPythonCommand`). If no syntax-specific command is found, the ST3 out-of-the-box
command `<Command>Command` (e.g. `FoldCommand`) is run instead.

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
Fold | ctrl+q, ctrl+f | yes | yes | `fold_dispatch`
Unfold | ctrl+q, ctrl+u | yes | yes | `unfold_dispatch`
Fold All | ctrl+q, ctrl+1 | yes | yes | `fold_by_level_dispatch`
Fold Level *n* | ctrl+q, ctrl+*n* | yes | yes | `fold_by_level_dispatch`
Unfold All | ctrl+q, ctrl+0 | yes | yes | `unfold_all_dispatch`

### Ditaa

Tool for creating image files from ascii diagrams using [ditaa](http://ditaa.sourceforge.net).
Looks for ditaa commands within comments in the current view, and creates the specified image file(s).

Setup:
Install the [Java](https://www.oracle.com/java/) runtime environment.
Make sure your PATH environment variable includes the path to the command-line java executable.
Download the [ditaa](http://ditaa.sourceforge.net) .jar and place it in the Packages/Ditaa folder.

Command | Keyboard shortcut | New<br />keyboard<br />shortcut<br />Windows | New<br />keyboard<br />shortcut<br />OSX | Implementation
------------ | ------------- | ------------- | ------------- | -------------
ditaa | (none) | n/a | n/a | `ditaa`

## Keyboard Shortcuts

Some background to the choice of keyboard shortcuts.

I like the Windows and OSX shortcuts to be as similar as possible,
and prefer Windows style shortcuts.

I can't type [properly](https://en.wikipedia.org/wiki/Touch_typing).
My 'home position' is to have the left thumb hovering over the shift and control keys in the bottom left,
and the three middle fingers of the right hand placed on the arrow keys in the bottom right.
I type mainly using the index and middle fingers.
I use the right thumb for the space bar.

I like the control key to be the leftmost key in the bottom row, just under the shift key.
If there is a different key in that position I will try to remap the keyboard
(e.g. using [Karabiner](https://pqrs.org/osx/karabiner) on the Mac).

The position of the alphanumeric keys are the ones least likely differ between keyboards.
The comma and period keys also seem fairly constantly placed.
I try to stay away from other keys for shortcuts.

I make use of prefixes (ctrl+q and ctrl+k) for some commands if they are rarely instantly repeated.

## Other plugins

### Visualize multi-selection

Make the cursor bolder when there is more than one selection region (`visualize_multiselect.py`)

## Syntax

### GText

File extension: `.gtxt`

A new syntax for simple markup of plain text files,
with the purpose of making them easy to read in Sublime.
Has specialized code folding.

### JapaneseText

File extension: `.jtxt`

An empty syntax definition with the sole purpose of recognizing Japanese text and use a different font
and font size.

### TSQL

File extensions: `.sql` `.tsql`

Transact-SQL syntax, based on ST3's SQL syntax 

### TSQLReport

File extensions: `.rpt` `.tsql.rpt`

A new syntax for Transact-SQL output.
Has specialized code folding.

## Theme

[Soda Dark](http://buymeasoda.github.io/soda-theme/)

## Colour Scheme

### Monokai Soda G

Based on [Monokai Soda](http://buymeasoda.github.com/soda-theme/extras/colour-schemes.zip).

## 3rd Party Packages

| Installed package
| -----------------
| [Package Control](https://packagecontrol.io/)
| [Package Resource Viewer](https://github.com/skuroda/PackageResourceViewer)
| [Omni Markup Previewer](http://theo.im/OmniMarkupPreviewer/)
| [Theme - Soda](http://buymeasoda.github.io/soda-theme/)
