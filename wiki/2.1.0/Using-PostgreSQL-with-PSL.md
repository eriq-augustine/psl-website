---
layout: wiki
---

In addition to [H2](http://www.h2database.com/html/main.html), PSL supports using [PostgreSQL](https://www.postgresql.org/) (or "Postgres" for short) as a database backend.
Often the slowest operation in PSL (and all SRL systems in general) is grounding.
PSL uses "bottom-up" grounding which formulates the grounding for each rule as a SQL query.
This means that the choice of database backend can have large performance impacts.

Note that the Postgres backend in PSL is relatively new and may have slight changes made to its interface.

## H2 vs Postgres
H2 is the default database backend for PSL.
H2 is an embedded database and therefore requires no additional installation or configuration, the entire engine ships with the PSL jar.
Databases are created as flat files (or fully in-memory).
This makes H2 more lightweight and easy to configure.
It is ideal for publishing experiments for papers that others may want to reproduce with ease.
H2 will also hold information and data in memory (the same memory space that your PSL program is in).
This makes certain operations fast:
 - Initiating a database operation (including a query).
 - Getting database/table metadata.
 - Inserting data.

However, the drawback of H2 is the same as its greatest asset... simplicity.
H2 has a simplified query planner, index structure, and data management.
As a result, it it often slow when queries get big (lots of ground rules) and/or complicated (rules with many atoms/predicates).
To counter these drawbacks, PSL also supports using a Postgres database backend.

Postgres follows the pattern of a more typical database engine where there is a service installed on some server (which may be the local machine) which accepts connections from clients.
Postgres is a production-grade, open source database engine and can easily scale into terabytes (but hopefully you are working with much less data).
Because Postgres is not embedded, it can be more complicated and robust.
The per-query overhead is higher with Postgres (because it needs to talk to another (possibly remote) process), but the queries typically run much faster.

For simple/small queries (ones that typically run in less than 10 seconds), we typically see H2 and Postgres preforming similarly (or H2 even faster).
However with larger queries, Postgres often runs 1-3 orders of magnitude faster.
The more data, the greater the difference between the two.
A general rule of thumb is that if you have more than 1 million groundings, consider switching to Postgres.

## Installing Postgres
We recommend at least Postgres v9.5.
The Postgres website has all the directions you should need for [installing Postgres](https://www.postgresql.org/download/).
If you still have issues, just try searching the internet for it.
Postgres is very popular, so the internet should have a wealth of answers for you.

## Setting Up The Database
Once you have Postgres installed, you need to setup a database and user.

### Security Note
In this section, we will assume that your Postgres instance is only accessible to the local machine and not open to the world.
If you want to open up your database please take the time to read up on the security implications for that.
For both performance and security reasons, we **strongly** recommend connecting to a database that is on the same machine and that only accepts local connections.
To accept all local connections, you can setup trust-based authentication in your Client Authentication Configuration File (usually called `pg_hba.conf`).
Adding this line to the bottom will let all local connections to connect.
```
local all all trust
```

### Database
Creating a database in Postgres can be done with the `createdb` command.
You can call your database whatever you want.

```sh
createdb psl
```

### User
Similar to creating a database, you can create a user with the `createuser` command.
It is easiest to create your psl user as a superuser (`-s`) so it can properly administrate the database.
However, people more versed in database administration can clamp down the permissions more tightly.

```sh
createuser -s jay
```

### Configuration
To get the most performance out of our database, we typically use some additional configuration options.
These are fully optional and PSL will run fine without them.
The general themes of the options are to increase the memory, decrease durability (since we will generally not need the database after PSL completes), and force some query plans.
These options should be in your `postgresql.conf` file.

```
# shared_buffers = 1/4 of system memory
# effective_cache_size = 1/2 of system memory
# For example, on a 16GB machine:
shared_buffers = 4GB
effective_cache_size = 8GB

# No Durability
fsync = off
full_page_writes = off
synchronous_commit = off

# Query Optimization
# Disable nested loops.
enable_nestloop = off

# Limit the write-ahead log (WAL)
# max_wal_size = 1/2 of shared_buffers
max_wal_size = 2GB
wal_buffers = 32MB
wal_level = minimal
max_wal_senders = 0
checkpoint_timeout = 30
```

## Using PostgreSQL in PSL

### Groovy
To use Postgres in the Groovy interface, just use the [PostgreSQLDriver](https://linqs-data.soe.ucsc.edu/psl-docs/docs/psl/develop-head/org/linqs/psl/database/rdbms/driver/PostgreSQLDriver.html) instead of the [H2DatabaseDriver](https://linqs-data.soe.ucsc.edu/psl-docs/docs/psl/develop-head/org/linqs/psl/database/rdbms/driver/H2DatabaseDriver.html).
There are various constructors that take in different information ranging from a database name to a full connection string.

```java
DataStore dataStore = new RDBMSDataStore(new H2DatabaseDriver(Type.Disk, "/tmp/psl", true), config);
```
```java
DataStore dataStore = new RDBMSDataStore(new PostgreSQLDriver("psl", true), config);
```

### CLI
To use Postgres in the CLI, just use the `--postgres` (`-p`) option.
This flag has one required argument, the name of the database to connect to.
This means that currently, you must be able to connect to that database as the current user (the one invoking PSL) without a password.

```sh
java -jar psl-cli-CANARY.jar --infer --data friendship.data --model friendship.psl --postgres psl
```