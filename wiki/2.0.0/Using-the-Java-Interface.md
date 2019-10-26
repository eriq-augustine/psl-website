---
layout: wiki
---

Application builders and advanced users can integrate PSL into their code as a library. Since the PSL codebase is organized as a Maven project, it is easiest to include PSL as a dependency via Maven.

### Integrating PSL via Maven

The [PSL codebase](https://github.com/linqs/psl.md) is organized as a Maven project with several subprojects. The subproject most likely of interest is `psl-core`, but stable versions of all the subprojects are published to the [PSL Maven repository](http://maven.linqs.org/repositories/psl-releases/.md). Including a PSL subproject in your Maven project is easy. It requires two steps

First, add `psl-core` (and any other subprojects) as dependencies to your `pom.xml` file:

```xml
<dependencies>
    ...
    <dependency>
        <groupId>org.linqs</groupId>
        <artifactId>psl-core</artifactId>
        <version>2.0.0</version>
    </dependency>
    ...
</dependencies>
```

Second, specify the location of the PSL Maven repository in your `pom.xml` file, anywhere within the `<project> </project>` tags:

```xml
<repositories>
	<repository>
		<releases>
			<enabled>true</enabled>
			<updatePolicy>daily</updatePolicy>
			<checksumPolicy>fail</checksumPolicy>
		</releases>
		<id>psl-releases</id>
		<name>PSL Releases</name>
		<url>http://maven.linqs.org/maven/repositories/psl-releases/</url>
		<layout>default</layout>
	</repository>
</repositories>
```

Maven will now make the the required PSL libraries and their dependencies available when compiling and running your project.