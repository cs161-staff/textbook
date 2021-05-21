---
title: 6. Cryptographic Definitions
parent: Cryptography
nav_order: 1
---

# Definitions

Intuitively, we can see that the Caesar cypher is not secure (try all 26
possible shifts and you'll get the original message back), but how can we prove
that it is insecure? To formally study cryptography, we will have to define a
mathematically rigorous framework that lets us analyze the security of various
cryptographic schemes.

## Alice, Bob, Eve, and Mallory

The most basic problem in cryptography is one of ensuring the security of
communications across an insecure medium. Two recurring members of the cast of
characters in cryptography are _Alice_ and _Bob_, who wish to communicate
securely as though they were in the same room or were provided with a dedicated,
untappable line. However, they only have available a telephone line or an
Internet connection subject to tapping by an eavesdropping adversary, _Eve_. In
some settings, Eve may be replaced by an active adversary _Mallory_, who can
tamper with communications in addition to eavesdropping on them.

The goal is to design a scheme for scrambling the messages between Alice and Bob
in such a way that Eve has no clue about the content of their exchange, and
Mallory is unable to tamper with the content of their exchange without being
detected. In other words, we wish to simulate the ideal communication channel
using only the available insecure channel.

## Keys

The most basic building block of any cryptographic system (or _cryptosystem_) is
the _key_. The key is a secret value that helps us secure messages. Many
cryptographic algorithms and functions require a key as input to lock or unlock
some secret value.

There are two main key models in modern cryptography. In the _symmetric key_
model, Alice and Bob both know the value of a secret key, and must secure their
communications using this shared secret value. In the _asymmetric key_ model,
each person has a secret key and a corresponding _public key_. You might
remember RSA encryption from CS 70, which is an asymmetric-key encryption
scheme.

## Confidentiality, Integrity, Authenticity

In cryptography, there are three main security properties that we want to
achieve.

_Confidentiality_ is the property that prevents adversaries from reading our
private data. If a message is confidential, then an attacker does not know its
contents. Most cryptographic algorithms that guarantee confidentiality work as
follows: Alice _encrypts_ a message by changing it into a scrambled form that
the attacker cannot read. She then sends this encrypted message over the
insecure channel to Bob. When Bob receives the encrypted message, he _decrypts_
the message by changing it back into its original form. We sometimes call the
message _plaintext_ when it is unencrypted and _ciphertext_ when it is
encrypted. Even if the attacker can see the encrypted ciphertext, they should
not be able to decrypt it back into the corresponding plaintext--only the
intended recipient, Bob, should be able to decrypt the message.

_Integrity_ is the property that prevents adversaries from tampering with our
private data. If a message has integrity, then an attacker cannot change its
contents without being detected.

_Authenticity_ is the property that lets us determine who created a given
message. If a message has authenticity, then we can be sure that the message was
written by the person who claims to have written it.

Most cryptographic algorithms that guarantee integrity and authenticity work as
follows: Alice generates a _tag_ or a _signature_ on a message.  She sends the
message with the tag to Bob. When Bob receives the message and the tag, he
verifies that the tag is valid for the message that was sent. If the attacker
modifies the message, the tag should no longer be valid, and Bob's verification
will fail. This will let Bob detect if the message has been altered and is no
longer the original message from Alice. The attacker should not be able to
generate valid tags for their malicious messages.

A related property that we may want our cryptosystem to have is _deniability_.
If Alice and Bob communicate securely, Alice might want to publish a message
from Bob and show it to a judge, claiming that it came from Bob. If the
cryptosystem has deniability, there is no cryptographic proof available to
guarantee that Alice's published message came from Bob. For example, consider a
case where Alice and Bob use the same key to generate a signature on a message,
and Alice publishes a message with a valid signature. Then the judge cannot be
sure that the message came from Bob--the signature could have plausibly been
created by Alice.

## Overview of schemes

We will look at cryptographic primitives that provide confidentiality,
integrity, and authentication in both the symmetric-key and asymmetric-key
settings.

| | Symmetric-key | Asymmetric-key |
| | :--------------------------------------- | :--------------------------------------------------- |
| Confidentiality | Symmetric-key encryption (e.g., AES-CBC) | Public-key encryption(e.g., El Gamal, RSA encryption) |
| Integrity and authentication | MACs (e.g., AES-CBC-MAC) | Digital signatures (e.g., RSA signatures) |

In symmetric-key encryption, Alice uses her secret key to encrypt a message, and
Bob uses the same secret key to decrypt the message.

In public-key encryption, Bob generates a matching public key and private key,
and shares the public key with Alice (but does not share his private key with
anyone). Alice can encrypt her message under Bob's public key, and then Bob will
be able to decrypt using his private key.  If these schemes are secure, then no
one except Alice and Bob should be able to learn anything about the message
Alice is sending.

In the symmetric-key setting, _message authentication codes (MACs)_ provide
integrity and authenticity. Alice uses her secret key to generate a MAC on her
message, and Bob uses the same secret key verify the MAC. If the MAC is valid,
then Bob can be confident that no attacker modified the message, and the message
actually came from Alice.

In the asymmetric-key setting, _public-key signatures_ (also known as digital
signatures) provide integrity and authenticity. Alice generates a matching
public key and private key, and shares the public key with Bob (but does not
share her private key with anyone). Alice computes a digital signature of her
message using her private key, and appends the signature to her message. When
Bob receives the message and its signature, he will be able to use Alice's
public key to verify that no one has tampered with or modified the message, and
that the message actually came from Alice.

We will also look at several other cryptographic primitives. These primitives
don't guarantee confidentiality, integrity, or authenticity by themselves, but
they have desirable properties that will help us build secure cryptosystems.
These primitives also have some useful applications unrelated to cryptography.

- _Cryptographic hashes_ provide a one way digest: They enable someone to
  condense a long message into a short sequence of what appear to be random
  bits. Cryptographic hashes are irreversible, so you can't go from the
  resulting hash back to the original message but you can quickly verify that a
  message has a given hash.

- Many cryptographic systems and problems need a lot of random bits.  To
  generate these we use a _pseudo random number generator_, a process which
  takes a small amount of true randomness and stretches it into a long sequence
  that should be indistinguishable from actual random data.

- _Key exchange_ schemes (e.g. Diffie-Hellman key exchange) allow Alice and Bob
  to use an insecure communication channel to agree on a shared random secret
  key that is subsequently used for symmetric-key encryption.

## Kerckhoff's Principle

Let's now examine the threat model, which in this setting involves answering the
question: How powerful are the attackers Eve and Mallory?

To consider this question, recall _Kerckhoff's principle_ from the earlier notes
about security principles:

> Cryptosystems should remain secure even when the attacker knows all internal
> details of the system. The key should be the only thing that must be kept
> secret, and the system should be designed to make it easy to change keys that
> are leaked (or suspected to be leaked). If your secrets are leaked, it is
> usually a lot easier to change the key than to replace every instance of the
> running software. (This principle is closely related to _Don't rely on
> security through obscurity._)

Consistent with Kerckhoff's principle, we will assume that the attacker knows
the encryption and decryption algorithms.[^1] The only information the attacker
is missing is the secret key.

## Threat models

When analyzing the confidentiality of an encryption scheme, there are several
possibilities about how much access an eavesdropping attacker Eve has to the
insecure channel:

1. Eve has managed to intercept a single encrypted message and wishes to recover
   the plaintext (the original message). This is known as a
   _ciphertext-only attack_.

2. Eve has intercepted an encrypted message and also already has some partial
   information about the plaintext, which helps with deducing the nature of the
   encryption. This case is a _known plaintext attack_. In this case Eve's
   knowledge of the plaintext is partial, but often we instead consider complete
   knowledge of one instance of plaintext.

3. Eve can capture an encrypted message from Alice to Bob and re-send the
   encrypted message to Bob again. This is known as a _replay attack_. For
   example, Eve captures the encryption of the message "Hey Bob's Automatic
   Payment System: pay Eve \$$100$" and sends it repeatedly to Bob so Eve gets
   paid multiple times. Eve might not know the decryption of the message, but
   she can still send the encryption repeatedly to carry out the attack.

4. Eve can trick Alice to encrypt arbitrary messages of Eve's choice, for which
   Eve can then observe the resulting ciphertexts. (This might happen if Eve
   has access to the encryption system, or can generate external events that
   will lead Alice to sending predictable messages in response.) At some other
   point in time, Alice encrypts a message that is unknown to Eve; Eve
   intercepts the encryption of Alice's message and aims to recover the message
   given what Eve has observed about previous encryptions. This case is known as
   a _chosen-plaintext attack_.

5. Eve can trick Bob into decrypting some ciphertexts. Eve would like to use
   this to learn the decryption of some other ciphertext (different from the
   ciphertexts Eve tricked Bob into decrypting).  This case is known as a
   _chosen-ciphertext attack_.

6. A combination of the previous two cases: Eve can trick Alice into encrypting
   some messages of Eve's choosing, and can trick Bob into decrypting some
   ciphertexts of Eve's choosing. Eve would like to learn the decryption of some
   other ciphertext that was sent by Alice. (To avoid making this case trivial,
   Eve is not allowed to trick Bob into decrypting the ciphertext sent by
   Alice.) This case is known as a _chosen-plaintext/ciphertext attack_, and is
   the most serious threat model.

Today, we usually insist that our encryption algorithms provide security against
chosen-plaintext/ciphertext attacks, both because those attacks are practical in
some settings, and because it is in fact feasible to provide good security even
against this very powerful attack model.

However, for simplicity, this class will focus primarily on security against
chosen-plaintext attacks.

[^1]:
    The story of the Enigma gives one possible justification for this
    assumption: given how widely the Enigma was used, it was inevitable that
    sooner or later the Allies would get their hands on an Enigma machine, and
    indeed they did.
