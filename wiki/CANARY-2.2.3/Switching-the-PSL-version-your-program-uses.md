---
layout: wiki
---

To change the [version](Change-Log.md) of PSL your project uses, edit your project's `pom.xml` file. The POM will declare dependencies on one or more PSL artifacts, e.g.,

```xml
<dependencies>
    ...
    <dependency>
        <groupId>org.linqs</groupId>
        <artifactId>psl-groovy</artifactId>
        <version>2.0.0</version>
    </dependency>
    ...
</dependencies>
```

Change the version element of each such dependency to a new version (all the same one) and rebuild.
See [Choosing a Version of PSL](Choosing-a-Version-of-PSL.md) to decide how to specify your version.