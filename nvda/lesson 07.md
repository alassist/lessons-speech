# Navigating through objects

NVDA has a navigation method which navigates through the objects, or
items, on the screen. Objects are items on the screen, like boxes to
type into, lists of items, a table, or a group of radio buttons. These
items can usually be interacted with using the system focus, but
sometimes cannot be.

Using object navigation, the Windows screen is shown in a tree, or
list. This means that at the top is one item, the root of the tree,
followed, below, by the items inside that list, or sublist, or the
branches on the tree. Lists may have items inside them, being the list
items. Tables have inside them the rows, then the cells of that row,
within the table, and inside the
cells is the text of the cell.

Rather than having to move back and forth between every single object
on the screen, however, the objects are organized hierarchically. This
means that some objects contain other objects, and you must move
inside them to access the objects they contain. For example, a list
contains list items, so you must move inside the list in order to
access its items. If you have moved to a list item, moving to the next
and previous item will take you to other list items in the same list.
Moving to a list item's containing object will take you back to the
list. You can then move past the list if you wish to access other
objects. Similarly, a toolbar contains controls, so you must move
inside the toolbar to access the controls in the toolbar. You can
review text inside the objects using the text review commands learned
in the previous lesson.

To navigate by object, use the following commands:

<table>
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
<tr>
<td>Report current object</td>
<td>NVDA+numpad5</td>
<td>NVDA+shift+o</td>
<td>none</td>
<td>Reports the current navigator object. Pressing twice spells the information, and pressing 3 times copies this object’s name and value to the clipboard.</td>
</tr>
<tr>
<td>Move to containing object</td>
<td>NVDA+numpad8</td>
<td>NVDA+shift+upArrow</td>
<td>flick up (object mode)</td>
<td>Moves to the object containing the current navigator object</td>
</tr>
<tr>
<td>Move to previous object</td>
<td>NVDA+numpad4</td>
<td>NVDA+shift+leftArrow</td>
<td>flick left (object mode)</td>
<td>Moves to the object before the current navigator object</td>
</tr>
<tr>
<td>Move to next object</td>
<td>NVDA+numpad6</td>
<td>NVDA+shift+rightArrow</td>
<td>flick right (object mode)</td>
<td>Moves to the object after the current navigator object</td>
</tr>
<tr>
<td>Move to first contained object</td>
<td>NVDA+numpad2</td>
<td>NVDA+shift+downArrow</td>
<td>flick down (object mode)</td>
<td>Moves to the first object contained by the current navigator object</td>
</tr>
<tr>
<td>Move to focus object</td>
<td>NVDA+numpadMinus</td>
<td>NVDA+backspace</td>
<td>none</td>
<td>Moves to the object that currently has the system focus, and also places the review cursor at the position of the System caret, if it is showing</td>
</tr>
<tr>
<td>Activate current navigator object</td>
<td>NVDA+numpadEnter</td>
<td>NVDA+enter</td>
<td>double tap</td>
<td>Activates the current navigator object (similar to clicking with the mouse or pressing space when it has the system focus)</td>
</tr>
<tr>
<td>Move System focus or caret to current review position</td>
<td>NVDA+shift+numpadMinus</td>
<td>NVDA+shift+backspace</td>
<td>none</td>
<td>pressed once Moves the System focus to the current navigator object, pressed twice moves the system caret to the position of the review cursor</td>
</tr>
<tr>
<td>Report review cursor location</td>
<td>NVDA+numpadDelete</td>
<td>NVDA+delete</td>
<td>none</td>
<td>Reports information about the location of the text or object at the review cursor. For example, this might include the percentage through the document, the distance from the edge of the page or the exact screen position. Pressing twice may provide further detail.</td>
</tr>
</tbody>
</table>

## Activity

Follow these steps to familiarize yourself with object navigation.
Please read the instructions before performing the steps.

* Press **Windows + R** to open a dialog box for entering a command to run.
* Type “winver” without the quotation marks. Be sure to type the command exactly as shown.
* Use object navigation to move to the “previous” item, and until you find the version of Windows you are running.
* Copy this information by using **Insert + F9** to mark the start of the text, moving with text review to the end of the line, and pressing **Insert + F10** twice quickly to copy the text to the clipboard.
* Press **Escape** to close the dialog box.
* Press **Windows + R** again.
* Type “notepad” without the quotes, and press **Enter** afterwards.
* Press **Control + V** to paste the information copied from the Windows Version dialog box
* Press **Alt + F4** to close notepad, and choose not to save the file.
