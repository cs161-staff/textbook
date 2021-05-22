---
title: 19. Elements of a Webpage
parent: Web Security
nav_order: 3
---

# Elements of a Webpage

The HTTP protocol is designed to return arbitrary files. The response header
usually specifies a [media type](https://en.wikipedia.org/wiki/Media_type) that
tells the browser how to interpret the data in the response body.

Although the web can be used to return files of any type, much of the web is
built in three languages that provide functionality useful in web applications.

A modern web page can be thought of as a distributed application: there is a
component running on the web server and a component running in the web browser.
First, the browser makes an HTTP request to a web server. The web server
performs some server-side computation and generates and sends an HTTP response.
Then, the browser performs some browser-side computation on the HTTP response
and displays the result to the user.

## HTML

HTML (Hypertext Markup Language) lets us create structured documents with
paragraphs, links, fillable forms, and embedded images, among other features.
You are not expected to know HTML syntax for this course, but some basics are
useful for some of the attacks we will cover.

Here are some examples of what HTML can do:

- Create a link to Google: `<a href="http://google.com">Click me</a>`

- Embed a picture in the webpage: `<img src="http://cs161.org/picture.png">`

- Include JavaScript in the webpage: `<script>alert(1)</script>`

- Embed the CS161 webpage in the webpage:
  `<iframe src="http://cs161.org"></iframe>`

Frames pose a security risk, since the outer page is now including an inner page
that may be from a different, possibly malicious source. To protect against
this, modern browsers enforce frame isolation, which means the outer page cannot
change the contents of the inner page, and the inner page cannot change the
contents of the outer page.

## CSS

CSS (Cascading Style Sheets) lets us modify the appearance of an HTML page by
using different fonts, colors, and spacing, among other features. You are not
expected to know CSS syntax for this course, but you should know that CSS is as
powerful as JavaScript when used maliciously. If an attacker can force a victim
to load some malicious CSS, this is functionally equivalent to the attacker
forcing the victim to load malicious JavaScript.

## JavaScript

JavaScript is a programming language that runs in your browser. It is a very
powerful language--in general, you can assume JavaScript can arbitrarily modify
any HTML or CSS on a webpage. Webpages can include JavaScript in their HTML to
allow for dynamic features such as interactive buttons. Almost all modern
webpages use JavaScript.

When a browser receives an HTML document, it first converts the HTML into an
internal form called the DOM (Document Object Model). The JavaScript is then
applied on the DOM to modify how the page is displayed to the user. The browser
then renders the DOM to display the result to the user.

Because JavaScript is so powerful, modern web browsers run JavaScript in a
sandbox so that any JavaScript code loaded from a webpage cannot access
sensitive data on your computer or even data on other webpages.

Most exploits targeting the web browser itself require JavaScript, either
because the vulnerability lies in the browser's JavaScript engine, or because
JavaScript is used to shape the memory layout of the program for improving the
success rate of an attack.

Almost all web browsers implement JavaScript as a Just In Time compiler,
dynamically converting JavaScript into machine code[^1]. Many modern desktop
applications (notably Slack's desktop client) are actually written in the
Electron framework, which is effectively a cut down web browser running
JavaScript.

[^1]:
    Trivia: Running JavaScript fast is considered so important that ARM recently
    introduced a dedicated instruction, FJCVTZS (Floating-point Javascript
    Convert to Signed fixed-point, rounding toward Zero), specifically to handle
    how JavaScript's math operates.
