---
layout: wiki
---

The following software is required to use PSL:

### Java 7 or 8 JDK
Ensure that the Java 7 or 8 development kit is installed.
Either [OpenJDK](http://openjdk.java.net/) or [Oracle Java](https://www.oracle.com/java/index.html) work.

We have had some reports of failing builds using Java prior to `1.7.0_110` or `1.8.0_110`.
If you have issues with Maven (especially handshake errors), try updating your version of java to at least `1.7.0_110` or `1.8.0_110`.
This is especially relevant for Mac users where the version of Java is less frequently updated.

#### Don't Build With Newer Versions of Java (9/10/11)

Building on newer versions of Java (9/10/11) can cause issues with the build system that may look strange and be hard to diagnose.
This means that building from source or the Java/Groovy interface should only be used with Java 7/8.
However, running the CLI should be possible on newer versions of Java.

### Maven 3.x
PSL uses [Maven](http://maven.apache.org) to manage builds and dependencies.
Users should [install Maven 3.x](http://maven.apache.org/download.html).
PSL is developed with Maven and PSL programs are created as Maven projects.
See [running Maven](http://maven.apache.org/run-maven/index.html) for help using Maven to build projects.