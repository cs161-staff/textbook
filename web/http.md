---
title: 20. HTTP
parent: Web Security
nav_order: 2
---

# HTTP

The protocol that powers the World Wide Web is the Hypertext Transfer Protocol,
abbreviated as HTTP. It is the language that clients use to communicate with
servers in order to fetch resources and issue other requests. While we will not
be able to provide you with a full overview of HTTP, this section is meant to
get you familiar with several aspects of the protocol that are important to
understanding web security.

## The Request-Response Model

Fundamentally, HTTP follows a request-response model, where clients (such as
browsers) must actively start a connection to the server and issue a request,
which the server then responds to. This request can be something like "Send me a
webpage" or "Change the password for my user account to `foobar`." In the first
example, the server might respond with the contents of the web page, and in the
second example, the response might be something as simple as "Okay, I've changed
your password." The exact structure of these requests will be covered in further
detail in the next couple sections.

The original version of HTTP, HTTP 1.1, is a text-based protocol, where each
HTTP request and response contains a _header_ with some metadata about the
request or response and a _payload_ with the actual contents of the request or
response. HTTP2, a more recent version of HTTP, is a binary-encoded protocol
for efficiency, but the same concepts apply.

For all requests, the server generates and sends a response. The response
includes a series of headers and, in the payload, the body of the data
requested.

## Structure of a Request

Below is a very simple HTTP request.

```
GET / HTTP/1.1
Host: squigler.com
Dnt: 1
```

The first line of the request contains the method of the request (`GET`), the
path of the request (`/`), and the protocol version (`HTTP/1.1`). This is an
example of a GET request. Each line after the first line is a request header. In
this example, there are two headers, the DNT header and the Host header. There
are many HTTP headers defined in the HTTP spec which are used to convey various
pieces of information, but we will only be covering a couple of them through
this lab.

Here is another HTTP request:

```
POST /login HTTP/1.1
Host: squigler.com
Content-Length: 40
Content-Type: application/x-url-formencoded
Dnt: 1

username=alice@foo.com&password=12345678
```

Here, we have a couple more headers and a different request type: the POST
request.

## GET vs. POST

While there are quite a few methods for requests, the two types that we will
focus on for this course are GET requests and POST requests. GET requests are
are generally intended for "getting" information from the server. POST requests
are intended for sending information to the server that somehow modifies its
internal state, such as adding a comment in a forum or changing your password.

In the original HTTP model, GET requests are not supposed to change any server
state. However, modern web applications often change server state in response to
GET requests in query parameters.

Of note, only POST requests can contain a body in addition to request headers.
Notice that the body of the second example request contains the username and
password that the user `alice` is using to log in. While GET requests cannot
have a body, it can still pass query parameters via the URL itself. Such a
request might look something like this:

```
GET /posts?search=security&sortby=popularity
Host: squigler.com
Dnt: 1
```

In this case, there are two query parameters, `search` and `sortby`, which have
values of `security` and `popularity`, respectively.
