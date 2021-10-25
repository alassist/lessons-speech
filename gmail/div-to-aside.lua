-- div-to-aside.lua
--
-- Pandoc filter which converts divs with an "aside" class into HTML `<aside>` elements.
--
-- To use it place the filter file in the folder you are running pandoc from and add 
-- "--lua-filter=div-to-aside.lua" (without the quotes) to the pandoc command line.

local List = assert(
  pandoc.List or require"pandoc.List",
  "Couldn't find pandoc.List"
)

local open_aside = pandoc.RawBlock('html', '<aside>')
local close_aside = pandoc.RawBlock('html', '</aside>')

function Div (div)
  -- Do nothing unless we have an "aside" class
  if not div.classes:includes("aside") then return nil end
  -- Initialize the list to be returned
  -- with the opening aside tag
  local aside = List:new{open_aside}
  -- Add the contents of the div
  aside:extend(div.content)
  -- Add the closing aside tag
  aside:extend{close_aside}
  -- replace the div with the aside
  return aside
end