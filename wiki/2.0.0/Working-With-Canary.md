---
layout: wiki
---

### What is Canary?
The Canary is a published build of PSL that is based on the development branch.
The name "Canary" comes from the iconic use of a [canary in a coal mine](https://en.wikipedia.org/wiki/Sentinel_species#Historical_examples) to detect toxic gas.
The build is somewhere near the tip of the development tree.
It is updated whenever the PSL developers feel a significant change has been made in development.

### Using Canary
The use canary, simply change your PSL version in your `pom.xml` to `CANARY`.
There is only one official Canary build (no version numbers).
We do not use version number on Canary, so you can always simply pull `CANARY` and be sure that you have the latest version.

```xml
<dependencies>
    ...
    <dependency>
        <groupId>org.linqs</groupId>
        <artifactId>psl-groovy</artifactId>
        <version>CANARY</version>
    </dependency>
    ...
</dependencies>
```

### How do I upgrade my Canary?
Since we do not use version numbers with CANARY, Maven will not fetch a new version unprompted.
To upgrade your canary build, delete the old Canary from your Maven cache.
On Lunix/Mac, this is: `~/.m2/repository/org/linqs/psl*/CANARY`