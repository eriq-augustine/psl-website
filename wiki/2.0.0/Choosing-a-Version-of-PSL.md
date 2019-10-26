---
layout: wiki
---

Maven allows [several ways](https://docs.oracle.com/middleware/1212/core/MAVEN/maven_version.htm#MAVEN402) to specify acceptable versions for dependencies.
This page discusses the recommended options to specifying the PSL version to use.

## Exact Version
If you are working on a paper or code that requires exact reproducibility, then you should specify an exact version of PSL.

For example:
```xml
<dependencies>
    ...
    <dependency>
        <groupId>org.linqs</groupId>
        <artifactId>psl-groovy</artifactId>
        <version>2.1.3</version>
    </dependency>
    ...
</dependencies>
```

## Major Minor
If you want to get bug fixes without worrying about breaking changes, then you can specify a major and minor version while allowing the incremental (patch) version to grow.

For example:
```xml
<dependencies>
    ...
    <dependency>
        <groupId>org.linqs</groupId>
        <artifactId>psl-groovy</artifactId>
        <version>[2.1,)</version>
    </dependency>
    ...
</dependencies>
```

## Major
If you want the latest stable code and can tolerate the occasional breakage, then you can specify just the major version.

For example:
```xml
<dependencies>
    ...
    <dependency>
        <groupId>org.linqs</groupId>
        <artifactId>psl-groovy</artifactId>
        <version>[2,)</version>
    </dependency>
    ...
</dependencies>
```

## Canary
If you are doing development any are willing to accept potential bugs, broken builds, and API breakages, then you can use the canary build.
See the [working with canary page](Working-With-Canary.md) to get detail on how best to work with the canary build.

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