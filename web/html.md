---
title: 14. Elements of a Webpage
parent: Web Security
nav_order: 3
---

# Elements of a Webpage

The HTTP protocol could only return plain text files, but to make the web more
interesting, we write webpages with three different languages that provide
additional functionality.

## HTML

HTML (Hypertext Markup Language) lets us create structured documents with
paragraphs, links, fillable forms, and embedded images, among other features.
You are not expected to know HTML syntax for this course, but some basics are
useful for some of the attacks we will cover.

Here are some examples of what HTML can do:

- Create a link to Google: `<a href="http://google.com">Click me</a>`
- Embed a picture in the webpage: `<img src="http://cs161.org/picture.png">`
- Include JavaScript in the webpage: `<script>alert(1)</script>`
- Embed the CS161 webpage in the webpage: `<iframe
  src="http://cs161.org"></iframe>`

Frames pose a security risk, since the outer page is now including an inner page
that may be from a different, possibly malicious source. To protect against
this, modern browsers enforce frame isolation, which means the outer page cannot
change the contents of the inner page, and the inner page cannot change the
contents of the outer page.

## CSS

CSS (Cascading Style Sheets) lets us modify the appearance of an HTML page by
using different fonts, colors, and spacing, among other features. You are not
expected to know CSS syntax for this course.

## JavaScript

JavaScript is a programming language that runs in your browser. It is a very
powerful language--in general, you can assume JavaScript can arbitrarily modify
any HTML or CSS on a webpage. Webpages can include JavaScript in their HTML to
allow for dynamic features such as interactive buttons.

Because JavaScript is so powerful, modern web browsers typically run JavaScript
in a sandbox so that any code from a webpage cannot access sensitive data on
your computer.
