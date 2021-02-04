---
title: 12. Intro to the Web
parent: Web Security
nav_order: 1
---

# Intro to the Web

It would not be too much of a stretch to say that much of today's world is built
upon the Internet. Many of the services that run on top of the Internet come
with their own class of vulnerabilities and defenses to match. In particular, we
will be focusing on web security, which covers a class of attacks that target
web pages and web services.

## URLs

Every resource (webpage, image, PDF, etc.) on the web is identified by a URL
(Uniform Resource Locator). A typical URL consists of three parts:

<p style="text-align: center">
  <code>
    <span style="color: blue">http</span
    >://<span style="color: green">www.example.com</span
    ><span style="color: red">/index.html</span>
  </code>
</p>

The protocol, <code style="color: blue">http</code>, tells your browser how to
retrieve the resource. In this class, the only two protocols you need to know
are HTTP, which we will cover in the next section, and HTTPS, which is a secure
version of HTTP using TLS (refer to the networking unit for more details).

The domain name, <code style="color: green">www.example.com</code>, tells your
browser which web server to contact to retrieve the resource.  Sometimes the
domain name will also include a port number, such as , to distinguish between
different applications running on the same web server.

The path, <code style="color: red">/index.html</code>, tells your browser which
page on the web server to request.  The web server uses the path to determine
which page or resource should be returned to you.

_Further reading:_ [What is a
URL?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL)
