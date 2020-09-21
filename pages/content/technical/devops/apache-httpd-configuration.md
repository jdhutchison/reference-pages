---
title: Apache HTTPd configuration
weight: 1
---

Useful notes
------------
[This page](https://www.whoishostingthis.com/resources/htaccess/) has lots of useful detail.

General redirects
-----------------
In `.htaccess` the format of a redirect rule is:
Redirect _[permanent]_ /[uri] http://[where to]
RedirectMatch _[permanent]_ ^/[regex]$ http://[where-to]/$1

The _permanent_ flag determines if the redirect is a 301 or a 302.
