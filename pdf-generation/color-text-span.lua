-- https://stackoverflow.com/questions/62831191/using-span-for-font-color-in-pandoc-markdown-for-both-html-and-pdf
-- https://bookdown.org/yihui/rmarkdown-cookbook/font-color.html
-- https://ulriklyngs.com/post/2019/02/20/how-to-use-pandoc-filters-for-advanced-customisation-of-your-r-markdown-documents/

function Span (el)
    local style = el.attributes.style
    if style and string.find(style, "color") then
      stylestr = style
      thecolor = string.match(stylestr, "color:%s*(%a+);?")

      local color_mapping = {
        blue = "blue",
        red = "purple", 
        green = "teal",
      }

      local latex_color = color_mapping[thecolor]

      --print(thecolor)
      if FORMAT:match 'latex' then
        -- encapsulate in latex code
        table.insert(
          el.content, 1,
          pandoc.RawInline('latex', '\\textcolor{'..latex_color..'}{')
        )
        table.insert(
          el.content,
          pandoc.RawInline('latex', '}')
        )
        -- returns only span content
        return el.content
      else
        -- for other format return unchanged
        return el
      end
    else
      return el
    end
  end