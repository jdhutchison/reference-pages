---
title: Ansible
weight: 1
---

Detecting if a service is running on a box
------------------------------------------

Use stat to check if there is an System V file for it, for example:

```yaml
- name: Check if PHP-FPM is present
stat:
path: /etc/init.d/php{{ php_version }}-fpm
register: php_fpm_present
```

