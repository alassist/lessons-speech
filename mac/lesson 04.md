# Lesson 4

In this lesson, you'll learn how to use the MacOS Finder. Finder is the Mac's file browser. With it, you can look at files and folders on internal, external, and network drives; copy, cut, and paste items; tag files for easier locating later; search for files; and more.

## For Windows Users

If you are switching from Windows to Mac, there are a few things you should know about the Finder. First, try very hard to get used to pressing command-o to open things. Pressing enter will prompt you to rename them, not open them. If you do accidentally press enter, simply press escape to cancel. Just like in Windows, you can bring up a context menu for any file or folder. Use control-option-shift-m, not shift-f10 or the applications key, but the end result is the same. As you will see later, there is very little interacting, VO-arrowing, or other special commands. For the most part, Finder is as simple as opening a folder, using up and down arrows to browse it, and opening the file you want, similar to Windows.

## View Setting

The most important part of Finder to understand is that Finder offers four possible ways in which to view your files and folders. Each has its good points, but the major advantages to these different views are visual. VoiceOver users are best served by picking a view and sticking with it, only using the others where necessary.

The two views that work best with VoiceOver are List View and Column View (command-2 and command-3, respectively). The main difference between them is that List View displays a list of the files and folders inside the parent folder only. Column View, on the other hand, displays a tree of all the items on the selected drive or location, letting you expand and collapse folders, but always showing every item. Our choice for now is List View, since it is limited to only the selected location and therefore offers less to deal with, but the best view for you is whichever you find you like more. For the rest of this course, we will ignore the other two views, as they make little sense for VoiceOver users. If an experience closer to File Explorer on Windows is what you are looking for, stick to List View.

## Copying and Pasting

This aspect of managing files and folders can be confusing at first, so I will explain how it works. When you paste an item in List View, it is put into the folder you have open at the time. If you paste in Column View, though, the item is put into the folder you are in only if you are pointing to another file. If you are pointing to (that is, focused on) a folder, your item will go into that folder instead of into the folder you have open. That is the other reason I prefer List View - pasting things is more straightforward and reliable.

Let me illustrate this with an example. Say you have a file in your Downloads folder, and you want to copy and paste it into a different folder. The first step is easy: navigate to the file and press command-c. To paste it, you go to the folder you want it in and press command-v (or command-option-v to move, rather than copy, the file).
In List View, you open up the folder by navigating to it and pressing command-o or command-down arrow. In Column View, though, you find the folder, then paste right there, without opening it. At first this sounds great, and it is fine so long as you are aware of what is going on. List View is a cleaner interface, but Column View works just as well once you understand it.

## Navigating

In List View, you open a folder or drive by pressing command-o or command-down arrow, and close with command-w. You can also expand a folder or drive in this view with the right arrow, and collapse it with the left arrow, which you may need to press twice.

In Column View, you expand a folder or drive with the right arrow, and collapse it with the left arrow, which you may need to press twice.

First letter navigation works as it does most anywhere in macOS. Namely, you can simply start typing the name of what you are looking for, and you will be moved there, if the item exists. The only confusing part of this is in Column View. When you expand a folder, that folder is expanded next time you view it, meaning that you can suddenly find yourself taken to an item within some random subfolder you had no idea was open. List View does not allow this, so you are always moving among only the items at your current level.

As you look through folders, you may think you have to interact with the list or table of files and folders, but you don't. You can simply open up folders and use up and down arrows to navigate them, no need to focus on and/or interact with anything. The only time you ever need to interact with a file list is to perform non-contiguous selections, or to examine how a particular name is spelled. As in most tables in macOS, you can use option-up to jump to the first item in a list, and option-down to jump to the last item.

## Folder Hotkeys

Finder includes several helpful shortcut keys to let you quickly jump to several folders on your mac. They are:

Home
: command-shift-h

Downloads
: command-option-l

Recents
: command-shift-f

iCloud Drive
: command-shift-i (OS X 10.10 and later, and only if you've enabled iCloud Drive in your iCloud preferences)

Documents
: command-shift-o

Desktop
: command-shift-d
Computer (listing all connected drives)
: command-shift-c
Airdrop
: command-shift-r
Network
: command-shift-k
Applications
: command-shift-a
Utilities
: command-shift-u

## Setting Your Default View

Now that you know how Column and List Views work, you may be wondering how you can set one or the other as your default. The process is not as straightforward as you might think, so before you run off to your Finder's Preferences, keep reading.

Finder remembers the view you select for every folder you open. You can set a default view for all subfolders of a folder, or of a drive, and that is as far as Finder will let you take the setting of default views. Put another way, you can set a preferred view for all the contents of any single drive, but if your Mac is opening a drive it's never seen before, it will default to Icon View (command-1). New users will, at the least, probably want to set their favorite view for their entire Mac internal drive, the one normally named Macintosh HD. To set the default view for any folder or drive:

1. Open Finder and navigate to the drive. I find the easiest way to do this is command-shift-c, then up or down arrow to the drive to which you want to assign a default view.
2. If you have not done so already, set the view you want to use by pressing command-2 or command-3.
3. Once you are focused on the drive, but have not yet opened or expanded it, press command-j.
4. In the "View Options" dialog that appears, choose to use whatever view is already in use as your default (it should be the first checkbox you find, called "open in [selected view]"). Set any other options you want, but the view is the main one for our purposes. Be sure to check the "Browse in [selected view]" box as well.
5. Go to the bottom of the window and hit the "Use as Defaults" button, then close the window.

That's it, all folders on that drive should now always open in the view you just set. Be sure to follow the above steps for any drive you will be using - externals, network drives or shares, and so on. Note that you cannot currently set Airdrop to use any view other than Grid View.

## Selecting

Selecting contiguous items is easy, just hold shift as you arrow. If you keep holding shift as you arrow in the opposite direction, you will de-select one item at a time, and pressing any arrow key by itself will de-select everything at once. Since you can use option-up or option-down to jump to the first or last item, you can add shift to either keystroke to select to the start or end.

Non-contiguous selections are more complex, but quite doable. Note that the below instructions are for OS X 10.9 Mavericks or above; if you are using a version below 10.9, replace vo-command-enter with vo-command-space. Also remember that "vo" here means to hold down the control and option keys.

1. Interact with the list of files/folders.
2. Find the first item you want to select, and press vo-command-enter.
3. Now vo-up or vo-down to the next item you want. Be careful not to use the arrows by themselves, or you will de-select everything.
4. Once you are on the second item, press vo-command-enter.
5. Once you have all the items you want, perform your action - delete, copy, whatever it is, it will apply to everything you just selected.

## Dealing with External Drives

Getting to your drive is as easy as command-shift-c. That will take you to a list of every internal and external drive connected to your Mac. This will use the view you have set on the drive on which macOS is installed (normally called Macintosh HD). Simply move to the drive you want to browse and open it in the usual way for the current view, like Command + O.

The first time you open any drive, it will appear in Icon View, which is Finder's default. Remember that when you set a default view, you did so for one drive; since the Mac has not seen your removable drive before, it has no way of knowing which view you want to use. Simply press command-2 or command-3 once you open the drive, or use the procedure outlined in the section on setting a default view, to have the new drive use the view you want.

You may also wish to have all your drives shown on the desktop. If so, press command-comma to open Finder's preferences, select the General button from the toolbar, and check all the items you want shown on the desktop. There are other preferences you may wish to change in here, such as the showing of file extensions (in the Advanced section).

To eject a drive, find it in the Computer window (command-shift-c) and press command-e. This ejects it, which you know was successful once the drive disappears from the list. VoiceOver will normally speak the name of the next drive in the list, or say "no row selected," or in some other way indicate that the drive is gone.

## Miscellaneous Commands

Here are a few commands you will find helpful. They can mostly be found in the drop down menus (vo-m) of Finder, if you forget any or want to see what else is available.

Delete item
: command-delete

Rename item
: enter
Open item
: command-o
Control-click item (open contextual menu)
: vo-shift-m
copy
: command-c
paste copy
: command-v
Paste, erasing original (equivalent to Windows cut)
: command-option-v
Go to path (you can type a folder path directly)
: command-shift-g
Open new Finder window
: command-n
Cycle between open windows
: command-accent, or command-shift-accent to move backward (same as most Mac apps)

