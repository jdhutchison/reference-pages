---
title: Git
weight: 1
---

Setting credentials
-------------------
For the username:

`git config user.name "<username>"`
`git config user.email "<email"`

Use the _--global_ flag to set it for git in general.

For the passwod:

`git config --global credential.helper store`

then

`git pull`

Merging
-------

To merge one branch into another:
```
git checkout <merge from>
git pull
git checkout <merge to>
git merge [--no-ff] <merge from>
```

Fold submodule into main repository
-----------------------------------

These commands will add a directory added as a submodile into the main repository:

```
git rm --cached <directory>
git add <directory>
```
