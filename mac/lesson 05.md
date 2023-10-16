# Lesson 5

In this lesson, you'll learn to use the Safari web browser. Safari is the Mac's default web browser, and it does all the usual web browser things - opens webpages, downloads files, plays audio, all that. It has some neat tricks, too, like the Reader that can show you only the meat of an article.

However, if you are coming to the Mac for the first time, especially from a Windows background, Safari can seem like a clunky app at best, and a totally unusable mess at worst. As with all things on the Mac, though, you just have to understand how and why it does what it does. Eventually, you will be flying through webpages again, and there are even some nice tricks that VoiceOver can pull off to make your life easier.

## How VoiceOver Sees Webpages

On Windows, webpages are parsed into what are essentially virtual documents. This is how you can move around with the arrow keys - your screen reader has taken the content of the page and rendered it to mimic a regular document. In Mac OS X 10.9 and earlier, VoiceOver takes a different tack: it leaves the content alone, and simply uses the same navigation commands you already know to let you move around it. VoiceOver sees every "chunk" as a separate element, from a link, to a heading, to a paragraph, to an item in a list. As with any window on the Mac, you use vo-left and vo-right (remember that "vo" means control and option) to move through these "chunks". Alternatively, turn Quick Nav on with the left and right arrows together, and simply use left or right arrow to move around.

Starting in OS X 10.10 Yosemite (released October 2014), Apple has added the same arrow key navigation that Windows users know and love to Safari. So long as you have disabled Quick Nav, you can move around a webpage with the arrow keys, optionally combined with modifiers, just like in a document. Move by character, word, or line; jump to the start or end of a line or the entire page; select by adding the shift key to any movement command. It all works in Safari the way you'd expect.

## navigating By Web Elements

A web element is an item by which you can move - heading, link, list, table, button, text field, and so forth. In Windows screen readers, you jump by these items with keys (h for heading, for instance). VoiceOver has several ways of doing the same thing.

## Quick Nav

As stated, press the left and right arrows to enable or disable Quick Nav. When enabled, you can use first-letter navigation just like in Windows. Furthermore, you can go to the Voiceover utility, choose Commanders in the table, and click the Quick Nav tab to customize which keys jump you to which items.

The only thing to be careful of in this mode is text entry; when you go to write something, be sure to disable Quick Nav, or you may find your focus jumping all over the place as each letter you press is interpreted as a command instead of a character. Note that this only applies if you arrowed or flicked to a form field. If you tabbed to a field, you can simply start typing, since Quick Nav will automatically turn itself off.

New Macs do not have this enabled by default. Open the VoiceOver Utility with vo-f8 (or vo-globe-8 if you're using a Mac with a Touch Bar), go to Commanders in the table, choose Quick Nav, and check the "Enable single-key webpage navigation when using Quick Nav" checkbox. You only have to do this once. Alternatively, you can toggle single-key webpage navigation from anywhere by pressing vo-q.

## VoiceOver Commands

If you would rather not deal with Quick Nav, you can use several built-in commands. Vo-command-h will move to the next heading, vo-command-l to the next link, vo-command-t to the next table, and more. This set of commands is not nearly as extensive as the set available in Quick Nav, and it cannot be customized, but it is sometimes faster and less frustrating to use, particularly for newer users. This way, you never accidentally leave Quick Nav on and start doing things you never intended to do.

## Other Commanders

Quick Nav is one commander, but you do have others. For instance, you could configure your mac so that control held down as you perform a one-finger flick down on your trackpad will jump to the next heading. Keyboard and Numpad commanders are also available, depending on your keyboard. This article is not a tutorial on commanders, but suffice it to say that the customization for jumping around pages is almost endless. You can learn more about this in this article about VoiceOver's commanders.

## The Rotor

Finally, you can use the rotor. With Trackpad Commander on, the same rotating and flicking gestures you may know from VoiceOver on an iPhone, iPod Touch, or iPad will work on the Mac. To enable this commander, hold down the VoiceOver keys and perform a clockwise turn with two fingers, like turning a small dial. If you want to turn it off, do the same thing, but counterclockwise.

If you lack a trackpad (built-in or bluetooth), or are not familiar with iOS, you can also use the rotor from the keyboard. Simply enable Quick Nav by pressing the left and right arrow keys simultaneously, and then change the rotor item with up-right or up-left, moving by that item with up or down. For example, once Quick Nav is on, you can press up-right or up-left until VoiceOver says "headings," then down arrow to move from one heading to the next.

## The Web Rotor

A different way to access items on the page is the Web Rotor, a feature similar to listing links and other elements in Windows screen readers. Press vo-u on a webpage and you are presented with a list of pretty much everything on that page, divided up by type. For instance, there is a list of headings, a list of links, a list of buttons, and so on. Use left and right arrows to move between the lists. Once in a list, either use up and down arrows to navigate, or simply start typing the text you are looking for and, as with any list on the Mac, you are taken to the first match with every character you type. Press enter to be moved right to the item you are focused on, or escape to close the web rotor without moving.

## Searching

If you happen to know the text you want to move to, you can search for it. As with any app on the Mac, press vo-f, type your text, and press enter. To find the next occurrence of that text, use vo-g; to find the previous occurrence, use vo-shift-g. It is worth noting that these commands are not specific to Safari, but will work just about everywhere across macOS.

## Links

When you are on a link, your first instinct may be to press space on it. On the Mac, though, space will only activate buttons, checkboxes, and other form elements. To open links, use enter instead. VO-space also works, as does up-down arrows if Quick Nav is on. It is preferable to use enter, though, because you can combine it with modifiers to do different things:

enter
: open link
Option-enter
: download linked file
Command-enter
: open link in new tab (does not auto-focus on new tab)

## Filling Out Forms

As on Windows, tab will move you around a webpage, letting you quickly tab from form field to form field. However, you must enable the setting first, which is why many people think it cannot be done. Simply go to Safari, press command-comma to open the settings, go to the Advanced tab, and check the "Press Tab to highlight each item on a webpage" checkbox. Command-w closes the settings, and you are ready to tab.

Not all webpages are accessible. Often, you will move to an edit field or checkbox, and VoiceOver will simply report the element, without telling you what it is for. This is because the web author did not properly label it. If you are a Jaws user, you may find that Voiceover offers no labels on pages where Jaws offers them. This is because Jaws is using the text around the form element to guess at the prompt, whereas VoiceOver (and even some other Windows screen readers) is not going to take a guess, but will instead only speak a prompt if one is explicitly provided. If an element lacks a prompt, simply vo-left or vo-right, or use plain arrow key navigation, to find out what is around it.

### Entering Text

On Windows, Jaws and NVDA both have a special mode that lets you enter text. When in this mode, keys pressed go right to the webpage instead of being interpreted as navigational commands. VoiceOver works exactly opposite: normally, keys go right to the page, so to type text you need only find a text field, and begin typing. If Quick Nav is enabled, though, your typing will be interpreted as commands, similar to Windows screen readers when text entry mode is off. It takes getting used to, but once you shed the habit of pressing enter each time you focus on an edit field, it becomes very convenient to enter text. Plus, even with Quick Nav off, you can still move by heading, link, and a few other elements, and you can navigate with the arrows to see the text around an input field without needing to switch modes at all. Remember, too, that if you tab to a form field, Quick Nav is automatically disabled for you.

### Dropdown Lists

They go by many names: select/selection lists, drop down lists, combo boxes, and more; VoiceOver calls them popup buttons. They are those lists of items you can choose from, such as picking your country and state. On the Mac, they are very easy to use: find one, and press vo-space, down arrow, or space (with Quick Nav on, you can also use the up and down arrows together). Once opened, use the arrow keys or the usual typing navigation available in any list or menu on the Mac to find the item you want. Press enter, space, vo-space, or up-down (Quick Nav only) to choose that item, and the list closes with the item now selected.

### Checkboxes and Radio buttons

Checkboxes and radio buttons are both selected in the usual way (space, vo-space, up-down with Quick Nav on, or double tapping with Trackpad Commander on). Note, though, that using space by itself will work, but not offer feedback. The other methods will cause VoiceOver to announce the selection you just made, but simply pressing space will make the selection while VoiceOver says nothing.

## Web Spots

A web spot is a way to mark a location on a page so you can go back to it later. For instance, you might mark the main portion of a cluttered page you often visit, or a heading with information that changes a lot.
Web spots are treated like a list you move through. To move forward a web spot, press vo-command-right bracket; to move left, vo-command-left bracket. To set the part of the page you are on as a new web spot, press vo-command-shift-right bracket; use left bracket instead to remove a spot while you are focused on it. That's all there is to it.
Important note: web spots do not work well on pages that update and change their length. For example, they will work on a page showing an article, but on a forum, new content will lengthen the page and move or break your web spots. In other words, they are useful, but do not work well on all pages.

## Dealing with Tables

Navigating a table is simple: the VoiceOver keys with the arrow keys will move cell by cell (E.G. vo-right moves right a cell, vo-down moves down a cell). While you are in a table, use vo-home or vo-end to jump to the top or bottom. Note that this is vo-globe-left or vo-globe-right on an Apple keyboard or Macbook.

A command not specific to Safari that may also be helpful is the command to toggle table interactability. When off, which it is by default, you will automatically begin reading the cells in a table as you move through a webpage with vo-left or vo-right. If you enable interaction required for a table, though, you will simply hear "table" as you move to that table (note that this is a case-by-case command, not a global toggle for all tables).

## Miscellaneous Commands

Here are a few other helpful commands. Some of these are in the Menu Bar (vo-m), while others are VoiceOver-specific.

vo-shift-u
: when on a link, this will speak the URL to which the link points. Tip: press this, then press vo-shift-c, to copy the link's URL to your clipboard without needn't to open the link at all.

vo-shift-m
: right clicks/control clicks a link

vo-f2 (or vo-globe-2 if you're using a Mac with a Touch Bar)
: speak title of current page

vo-shift-i
: speaks the webpage title, then the number of links, headings, and so on

command-l
: open a new location (in the current tab); this also speaks the URL of the current page and lets you copy it to the clipboard

command-t
: open a new tab

command-w
: close current tab

control-tab
: next tab

control-shift-tab
: previous tab

command-d
: save the current page to favorites

command-option-l
: view downloads (interact with the table, then the group of a download, to view details)

command-left bracket
: back a page
command-right bracket
: forward a page

command-r
: refresh the page
command-period
: stop page loading
command-shift-r
: toggle Reader, if available (strips out all but the main text of a page)
command-shift-backslash (OS 10.10 and above)
: toggle showing all open tabs in a single window. This window includes tabs open on your Mac as well as on other devices connected to your Apple ID, and has a search field.
