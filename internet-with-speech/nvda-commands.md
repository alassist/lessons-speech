# NVDA keyboard commands

## Browse Mode

| Name                         | Key            | Description                                                                                                                                          |
|------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Toggle browse/focus modes    | NVDA+space     | Toggles between focus mode and browse mode                                                                                                           |
| Exit focus mode              | escape         | switches back to browse mode if focus mode was previously switched to automatically                                                                  |
| Refresh browse mode document | NVDA+f5        | Reloads the current document content (useful if certain content seems to be missing from the document. Not available in Microsoft Word and Outlook.) |
| Find                         | NVDA+control+f | Pops up a dialog in which you can type some text to find in the current document                                                                     |
| Find next                    | NVDA+f3        | Finds the next occurrence of the text in the document that you previously searched for                                                               |
| Find previous                | NVDA+shift+f3  | Finds the previous occurrence of the text in the document you previously searched for                                                                |
| open long description        | NVDA+d         | Opens a new window containing a long description for the element you are on if it has one.                                                           |

### Single Letter Navigation

While in browse mode, For quicker navigation, NVDA also provides single
character keys to jump to certain fields in the document. Note that not
all of these commands are supported in every type of document.

The following keys by themselves jump to the next available element,
while adding the shift key causes them to jump to the previous element:

h
:   heading

l
:   list

i
:   list item

t
:   table

k
:   link

n
:   nonLinked text

f
:   form field

u
:   unvisited link

v
:   visited link

e
:   edit field

b
:   button

x
:   checkbox

c
:   combo box

r
:   radio button

q
:   block quote

s
:   separator

m
:   frame

g
:   graphic

d
:   landmark

o
:   embedded object

1 to 6
:   headings at levels 1 to 6 respectively

To move to the beginning or end of containing elements such as lists and
tables:

| Name                       | Key         | Description                                                                           |
|----------------------------|-------------|---------------------------------------------------------------------------------------|
| Move to start of container | shift+comma | Moves to the start of the container (list, table, etc.) where the caret is positioned |
| Move past end of container | comma       | Moves past the end of the container (list, table, etc.) where the caret is positioned |

### The Elements List

The elements list provides access to a list of either links, headings or
landmarks in the document. Radio buttons allow you to switch between
these three types of information. An edit field is also provided in the
dialog which allows you to filter the list to help you search for a
particular item on the page. Once you have chosen an item, you can use
the provided buttons in the dialog to move to or activate that item. For
faster, and easier navigation to a specific place on the page, the Find
dialog box is recommended.

| Name                      | Key     | Description                                                                                        |
|---------------------------|---------|----------------------------------------------------------------------------------------------------|
| Browse mode elements list | NVDA+f7 | Brings up the Elements list which contains links, headings and landmarks from the current document |

### Embedded Objects

Pages can include rich content using technologies such as Adobe Flash
and Sun Java, as well as applications and dialogs. Where these are
encountered in browse mode, NVDA will report "embedded object",
"application" or "dialog", respectively. You can press enter on
these objects to interact with them. If it is accessible, you can then
tab around it and interact with it like any other application. A key
command is provided to return to the original page containing the
embedded object:

| Name                                    | Key                | Description                                                                               |
|-----------------------------------------|--------------------|-------------------------------------------------------------------------------------------|
| Move to containing browse mode document | NVDA+control+space | Moves the focus out of the current embedded object and into the document that contains it |
