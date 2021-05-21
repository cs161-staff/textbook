---
title: Cryptography
nav_order: 3
has_children: true
---

# Introduction

In this unit, we'll be studying _cryptography_, techniques for securing
information and communication in the presence of an attacker. In particular, we
will see how we can prevent adversaries from reading or altering our private
data. In a nutshell, cryptography is about communicating securely over insecure
communication channels.

The ideas we'll examine have significant grounding in mathematics, and in
general constitute the most systematic and formal set of approaches to security
that we'll cover.

## Disclaimer: Don't try this at home!

In this class, we will teach you the basic building blocks of cryptography, and
in particular, just enough to get a feeling for how they work at a conceptual
level. Understanding cryptography at a conceptual level will give you good
intuition for how industrial systems use cryptography in practice.

However, cryptography in practice is very tricky to get right. As
[@SwiftOnSecurity](https://twitter.com/swiftonsecurity) puts it, "Cryptography
is magic math that cares what color of pen you use." Actual real-world
cryptographic implementations require attention to a lot of details and hundreds
of possible pitfalls. For example, private information might leak out through
various side-channels, random number generators might go wrong, and
cryptographic primitives might lose all security if you use them the wrong way.
We won't have time to teach all of those details and pitfalls to you in CS 161,
so you should never implement your own cryptography using the algorithms we
teach you in this class.

Instead, the cryptography we show you in this class is as much about educating
you as a consumer as educating you as an engineer. If you find yourself needing
an encrypted connection between two computers, or if you need to send an
encrypted message to another person, you should use existing well-vetted
cryptographic tools. However, you will often be faced with the problem of
understanding how something is supposed to work. You might also be asked to
evaluate the difference between alternatives. For that, you will need to
understand the underlying cryptographic engineering involved. Similarly, there
are sometimes applications that take advantage of cryptographic primitives in
non-cryptographic ways, so it is useful to know the primitives. You never know
when you might need a hash, an HMAC, or a block cipher for a non-security task
that takes advantage of their randomness properties.

In summary, know that we're going to teach you just enough cryptography to be
dangerous, but not enough to implement industrial-strength cryptography in
practice.

## Brief History of Cryptography

The word "cryptography" comes from the Latin roots _crypt_, meaning secret, and
_graphia_, meaning writing. So cryptography is literally the study of how to
write secret messages.

Schemes for sending secret messages go back to antiquity. 2,000 years ago,
Julius Caesar employed what's today referred to as the "Caesar cypher," which
consists of permuting the alphabet by simply shifting each letter forward by a
fixed amount. For example, if Caesar used a shift by $$3$$ then the message
"cryptography" would be encoded as "fubswrjudskb". With the development of the
telegraph (electronic communication) during the 1800s, the need for encryption
in military and diplomatic communications became particularly important. The
codes used during this "pen and ink" period were relatively simple since
messages had to be decoded by hand. The codes were also not very secure, by
modern standards.

The second phase of cryptography, the "mechanical era," was the result of a
German project to create a mechanical device for encrypting messages in an
unbreakable code. The resulting _Enigma_ machine was a remarkable engineering
feat. Even more remarkable was the massive British effort during World War II to
break the code. The British success in breaking the Enigma code helped influence
the course of the war, shortening it by about a year, according to most experts.
There were three important factors in the breaking of the Enigma code. First,
the British managed to obtain a replica of a working Enigma machine from Poland,
which had cracked a simpler version of the code. Second, the Allies drew upon a
great deal of brainpower, first with the Poles, who employed a large contingent
of mathematicians to crack the structure, and then from the British, whose
project included Alan Turing, one of the founding fathers of computer science.
The third factor was the sheer scale of the code-breaking effort. The Germans
figured that the Enigma was well-nigh uncrackable, but what they didn't figure
on was the unprecedented level of commitment the British poured into breaking
it, once codebreakers made enough initial progress to show the potential for
success. At its peak, the British codebreaking organization employed over 10,000
people, a level of effort that vastly exceeded anything the Germans had
anticipated. They also developed electromechanical systems that could, in
parallel, search an incredible number of possible keys until they found the
right one.

Modern cryptography is distinguished by its reliance on mathematics and
electronic computers. It has its early roots in the work of Claude Shannon
following World War II. The analysis of the _one-time pad_ (discussed later in
these notes) is due to Shannon. The early 1970s saw the the introduction by NIST
(the National Institute for Standards in Technology) of a standardized
cryptosystem, _DES_. DES answered the growing need for digital encryption
standards in banking and other business. The decade starting in the late 1970s
then saw an explosion of work on a computational theory of cryptography.
