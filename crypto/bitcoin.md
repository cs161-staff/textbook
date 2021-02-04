---
title: 11. Bitcoin
parent: Cryptography
nav_order: 6
---

TODO: Draft I found in the fa19 repo. Incomplete and not sure if it ever was
finished. We should finish it this semester -peyrin sp21

# Welcome To Bitcoin

## Editorial

Bitcoin and other cryptocurrencies are very interesting from both a social and
technical viewpoint. Yet interesting does not necessarily mean "good". Bitcoin
technologically is a fairly simple idea: combining a public ledger with proof of
work. Yet it is a remarkably poor currency, a horrid store of value, and
surrounded by a community best described as "Bat Shit Insane".

There are also a lot of rather obscure details in Bitcoin itself, such as the
particular signature scheme and the use of double-hashing when a single hash
would suffice. We will skip over some of those details and present things at a
slightly higher level.

## Preliminary: Public Key Signatures

By this point in the class you should already have seen public key cryptography
and hash functions. Public key signatures are almost the same as public key
encryption, except backwards. Rather than creating a message that only the
private key holder can read, public key signatures are about creating a message
that only the private key holder could produce. Thus the signing function takes
a private key and a message (usually a cryptographic hash of the actual message)
to produce a signature, while the verification function takes the corresponding
public key and the signature to validate it.

## The Bitcoin Public Ledger

A Bitcoin "wallet" does not actually store Bitcoin. Instead it simply contains a
set of one or more private keys. The hash of the corresponding public key (with
suitable checksumming to prevent some typos) is the corresponding "address"
where others can send payment. For example, this public address
1FuckBTCqwBQexxs9jiuWTiZeoKfSo9Vyi[^1] has a corresponding private key.

Spending Bitcoin is in many ways analogous to simply writing a check. If the
address 1FuckBTC\... wants to send .052 Bitcoin to 1Ross5\..., the person who
controls 1FuckBTC simply signs a message to the effect of "conduct this
payment". The resulting hash

[d6b24ab29fa8e8f2c43bb07a3437538507776a671d9301368b1a7a32107b7139](https://blockchain.info/tx/d6b24ab29fa8e8f2c43bb07a3437538507776a671d9301368b1a7a32107b7139?show_adv=true)

[^1]:
    Created by Nick Weaver by simply generating a large number of random private
    keys until random luck generated one with the "FuckBTC" prefix
