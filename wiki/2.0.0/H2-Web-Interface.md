---
layout: wiki
---

If you use H2 as the backend database for PSL (as is done in the examples), it can be helpful to open up the resulting database and examine it for debugging purposes.

# Prerequisites

You should set up your PSL program to use H2 on disk and note where it is stored. For example, if you create your DataStore using the following code
```java
DataStore data = new RDBMSDataStore(new H2DatabaseDriver(Type.Disk, "/home/steve/psl", true), config);
```
then PSL will create an H2 database in the file `/home/steve/psl/psl.mv.db`. Then, run your program so the resulting H2 database can be inspected.

# Starting the H2 Web Server

You will need to use the H2 jar for your classpath. This is likely `~/.m2/repository/com/h2database/h2/1.4.192/h2-1.4.192.jar`, but you will need to modify it if, for example, you're using a different version of H2. You start the H2 web server by running the following command:
```
java -cp ~/.m2/repository/com/h2database/h2/1.4.192/h2-1.4.192.jar org.h2.tools.Server
```

# Using the H2 Web Server

Once you have started the web server, you can access it at `http://localhost:8082`. To log in, you should change the connection string to point to your H2 database file _without .mv.db on the end_. The username and password are both empty strings.