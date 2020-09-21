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

Reset root password
-------------------

First run:

```bash
mkdir /var/run/mysqld
chown mysql:mysql /var/run/mysqld
mysqld_safe --skip-grant-tables --skip-networking &
```

Then connect using `mysql` and run

```sql
use mysql;
update user set authentication_string=password('NEWPASSWORD') where user='root';
flush privileges;
quit
```
