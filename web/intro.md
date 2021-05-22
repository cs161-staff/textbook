---
title: 17. Intro to the Web
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
(Uniform Resource Locator). URLs are designed to describe exactly where to find
a piece of information on the Internet. A basic URL consists of three mandatory
parts:

<p style="text-align: center">
  <code>
    <span style="color: blue">http</span
    >://<span style="color: green">www.example.com</span
    ><span style="color: red">/index.html</span>
  </code>
</p>

The first mandatory part is the _protocol_, located before in the URL. In the
example above, the protocol is <code style="color: blue">http</code>. The
protocol tells your browser how to retrieve the resource. In this class, the
only two protocols you need to know are HTTP, which we will cover in the next
section, and HTTPS, which is a secure version of HTTP using TLS (refer to the
networking unit for more details). Other protocols include `git+ssh://`, which
fetches a git archive over an encrypted tunnel using `ssh`, or `ftp://`, which
uses the old FTP (File Transfer Protocol) to fetch data.

The second mandatory part is the _location_, located after but before the next
forward slash in the URL. In the example above, the location is
<code style="color: green">www.example.com</code>. This tells your browser which
web server to contact to retrieve the resource.

Optionally, the location may contain an optional _username_, which is followed
by an `@` character if present. For example,
<code style="color: green">evanbot@www.example.com</code> is a location with a
username `evanbot`. All locations must include a computer identifier. This is
usually a domain name such as <code style="color: green">www.example.com</code>.
Sometimes the location will also include a port number, such as
<code style="color: green">www.example.com:81</code>, to distinguish between
different applications running on the same web server. We will discuss ports a
bit more when we talk about TCP during the networking section.

The third mandatory part is the _path_, located after the first single forward
slash in the URL. In the example above, the path is
<code style="color: red">/index.html</code>. The path tells your browser which
resource on the web server to request. The web server uses the path to determine
which page or resource should be returned to you.

One way to think about paths is to imagine a filesystem on the web server you're
contacting. The web server can use the path as a filepath to locate a specific
page or resource. The path must at least consist of `/`, which is known as the
"root"[^1] of the filesystem for the remote web site.

Optionally, there can be a `?` character after the path. This indicates that you
are supplying additional arguments in the URL for the web server to process.
After the `?` character, you can supply an optional set of _parameters_
separated by `&` characters. Each parameter is usually encoded as a key-value
pair in the format `key=value`. Your browser sends all this information to the
web server when fetching a URL. See the next section for more details on URL
parameters.

Finally, there can be an optional _anchor_ after the arguments, which starts
with a `#` character. The anchor text is not sent to the server, but is
available to the web page as it runs in the browser.

The anchor is often used to tell your browser to scroll to a certain part of the
webpage when loading it. For example, try loading
<https://en.wikipedia.org/wiki/Dwinelle_Hall#Floor_plan> and
<https://en.wikipedia.org/wiki/Dwinelle_Hall#Construction> and note that your
browser skips to the section of the article specified in the anchor.

In summary, a URL with all elements present may look like this:

<p style="text-align: center">
  <code>
    <span style="color: blue">http://</span
    ><span style="color: red">evanbot@</span
    ><span style="color: blue">www.cs161.org</span
    ><span style="color: red">:161</span
    ><span style="color: blue">/whoami</span
    ><span style="color: red">?k1=v1&amp;k2=v2</span
    ><span style="color: blue">#anchor</span>
  </code>
</p>

where <code style="color: blue">http</code> is the protocol,
<code style="color: red">evanbot</code> is the username,
<code style="color: blue">www.cs161.org</code> is the computer location
(domain), <code style="color: red">161</code> is the port,
<code style="color: blue">/whoami</code> is the path,
<code style="color: red">k1=v1&amp;k2=v2</code> are the URL arguments, and
<code style="color: blue">anchor</code> is the anchor.

_Further reading:_ [What is a
URL?](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL)

[^1]:
    It is called the root because the filesystem can be treated as a tree and
    this is where the tree starts.
