---
layout: wiki
---

## What is Canary?
The Canary is a published build of PSL that is based on the development branch.
The name "Canary" comes from the iconic use of a [canary in a coal mine](https://en.wikipedia.org/wiki/Sentinel_species#Historical_examples) to detect toxic gas.
The build is somewhere near the tip of the development tree.
It is updated whenever the PSL developers feel a significant change has been made in development.

## Versioned vs Unversioned Canary
To make using the canary build easier for PSL users, we release **two** versions of the canary build in parallel.
On version is always called `CANARY` and will replace the previous build.
The other version will be called `CANARY-X.Y.Z` where `X.Y` matches the major/minor number of the next stable release and `Z` just increments by one for each canary build.

Unfortunately, we do not yet have any fancy infrastructure to check what canary versions are available, so the easiest way will be to just look at the [maven repository](https://linqs-data.soe.ucsc.edu/maven/repositories/psl-releases/org/linqs/psl-groovy/).

If you always want the latest and are willing to have potential incompatibilities between updates, use the unversioned canary.
If you want a newer version but don't want it to update or you are collaborating with other people, use the versioned canary.

## Using Canary

### Groovy

The use canary, simply change your PSL version in your `pom.xml` to `CANARY` or `CANARY-X.Y.Z` (with the proper substitution for `X.Y.Z`).

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

```xml
<dependencies>
    ...
    <dependency>
        <groupId>org.linqs</groupId>
        <artifactId>psl-groovy</artifactId>
        <version>CANARY-2.1.0</version>
    </dependency>
    ...
</dependencies>
```

### CLI

Using the canary in the CLI just means grabbing the new jar file from the [Maven repository](https://linqs-data.soe.ucsc.edu/maven/repositories/psl-releases/org/linqs/psl-cli).

### How do I update my Canary?
If you are using the versioned canary, then just update your version numbers in your pom.
If you are using the unversioned canary, then you will have to delete the old canary from your Maven cache.
On Lunix/Mac, this is at: `~/.m2/repository/org/linqs/psl*/CANARY`