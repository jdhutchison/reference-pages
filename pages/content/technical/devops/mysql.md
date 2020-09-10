---
title: MySQL
weight: 1
---

Code snippet and scripts for working with MySQL databases

Creating new SQL database and user
----------------------------------

```sql
create database (dbname);
grant usage on *.* to (dbname)@localhost identified by '(dbpass)';
grant all privileges on (dbname).* to (dbname)@localhost;
```
