Reviewing Text with NVDA
========================

Sometimes, using the arrow keys to read text isn’t what you want, or can do, to review text in the program you’re in. Othertimes, you may wish to review text on another line than the one you’re on, without moving from the spot which your cursor is on.

NVDA provides a mechanism for reviewing the current control, web page, document, or text area. This is called the Review Cursor, and is different from the Windows text cursor which you use with the Arrow keys.

Review Cursor Keys
==================

The following table contains NVDA functions, and the ways to use them, either through a Desktop keyboard, laptop keyboard, or touch screen.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Desktop key</th>
<th>Laptop key</th>
<th>Touch</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Switch to next review mode</td>
<td>NVDA+numpad7</td>
<td>NVDA+pageUp</td>
<td>2-finger flick up</td>
<td>switches to the next available review mode</td>
</tr>
<tr class="even">
<td>Switch to previous review mode</td>
<td>NVDA+numpad1</td>
<td>NVDA+pageDown</td>
<td>2-finger flick down</td>
<td>switches to the previous available review mode</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Desktop key</th>
<th>Laptop key</th>
<th>Touch</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Move to top line in review</td>
<td>shift+numpad7</td>
<td>NVDA+control+home</td>
<td>none</td>
<td>Moves the review cursor to the top line of the text</td>
</tr>
<tr class="even">
<td>Move to previous line in review</td>
<td>numpad7</td>
<td>NVDA+upArrow</td>
<td>flick up (text mode)</td>
<td>Moves the review cursor to the previous line of text</td>
</tr>
<tr class="odd">
<td>Report current line in review</td>
<td>numpad8</td>
<td>NVDA+shift+.</td>
<td>none</td>
<td>Announces the current line of text where the review cursor is positioned. Pressing twice spells the line. Pressing three times spells the line using character descriptions.</td>
</tr>
<tr class="even">
<td>Move to next line in review</td>
<td>numpad9</td>
<td>NVDA+downArrow</td>
<td>flick down (text mode)</td>
<td>Move the review cursor to the next line of text</td>
</tr>
<tr class="odd">
<td>Move to bottom line in review</td>
<td>shift+numpad9</td>
<td>NVDA+control+end</td>
<td>none</td>
<td>Moves the review cursor to the bottom line of text</td>
</tr>
<tr class="even">
<td>Move to previous word in review</td>
<td>numpad4</td>
<td>NVDA+control+leftArrow</td>
<td>2-finger flick left (text mode)</td>
<td>Moves the review cursor to the previous word in the text</td>
</tr>
<tr class="odd">
<td>Report current word in review</td>
<td>numpad5</td>
<td>NVDA+control+.</td>
<td>none</td>
<td>Announces the current word in the text where the review cursor is positioned. Pressing twice spells the word. Pressing three times spells the word using character descriptions.</td>
</tr>
<tr class="even">
<td>Move to next word in review</td>
<td>numpad6</td>
<td>NVDA+control+rightArrow</td>
<td>2-finger flick right (text mode)</td>
<td>Move the review cursor to the next word in the text</td>
</tr>
<tr class="odd">
<td>Move to start of line in review</td>
<td>shift+numpad1</td>
<td>NVDA+home</td>
<td>none</td>
<td>Moves the review cursor to the start of the current line in the text</td>
</tr>
<tr class="even">
<td>Move to previous character in review</td>
<td>numpad1</td>
<td>NVDA+leftArrow</td>
<td>flick left (text mode)</td>
<td>Moves the review cursor to the previous character on the current line in the text</td>
</tr>
<tr class="odd">
<td>Report current character in review</td>
<td>numpad2</td>
<td>NVDA+.</td>
<td>none</td>
<td>Announces the current character on the line of text where the review cursor is positioned. Pressing twice reports a description or example of that character. Pressing three times reports the numeric value of the character in decimal and hexadecimal.</td>
</tr>
<tr class="even">
<td>Move to next character in review</td>
<td>numpad3</td>
<td>NVDA+rightArrow</td>
<td>flick right (text mode)</td>
<td>Move the review cursor to the next character on the current line of text</td>
</tr>
<tr class="odd">
<td>Move to end of line in review</td>
<td>shift+numpad3</td>
<td>NVDA+end</td>
<td>none</td>
<td>Moves the review cursor to the end of the current line of text</td>
</tr>
<tr class="even">
<td>Say all with review</td>
<td>numpadPlus</td>
<td>NVDA+shift+a</td>
<td>3-finger flick down (text mode)</td>
<td>Reads from the current position of the review cursor, moving it as it goes</td>
</tr>
<tr class="odd">
<td>Select then Copy from review cursor</td>
<td>NVDA+f9</td>
<td>NVDA+f9</td>
<td>none</td>
<td>Starts the select then copy process from the current position of the review cursor. The actual action is not performed until you tell NVDA where the end of the text range is</td>
</tr>
<tr class="even">
<td>Select then Copy to review cursor</td>
<td>NVDA+f10</td>
<td>NVDA+f10</td>
<td>none</td>
<td>On the first press, text is selected from the position previously set start marker up to and including the review cursor’s current position. After pressing this key a second time, the text will be copied to the Windows clipboard</td>
</tr>
<tr class="odd">
<td>Report text formatting</td>
<td>NVDA+f</td>
<td>NVDA+f</td>
<td>none</td>
<td>Reports the formatting of the text where the review cursor is currently situated. Pressing twice shows the information in browse mode</td>
</tr>
<tr class="even">
<td>Report current symbol replacement</td>
<td>None</td>
<td>None</td>
<td>none</td>
<td>Speaks the symbol where the review cursor is positioned. Pressed twice, shows the symbol and the text used to speak it in browse mode.</td>
</tr>
</tbody>
</table>

Review modes
------------

NVDA’s text review function has a few modes which control how much can
be reviewed. One can use the following keys to control this:




Uses For Reviewing Text
=======================

There are a few cases for why reviewing text with the review cursor
can be useful.

* If you use the command line, or Windows terminal, you will need to
  review output with the review cursor, as the arrow keys move through
  history and the characters of your command.
* If you are in a document, you may want to review a prior line, or
  one below the current line.
* If you move, using the navigator object discussed later, you will
  have to review that line using the review cursor.

Activity
--------

- Use the review cursor to read the line above this one, then use
  **Insert + Up Arrow** to verify that your system cursor is still on
  this line.

You may practice with this to gain further experience with it.
