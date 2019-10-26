---
layout: wiki
---

[MOSEK](http://www.mosek.com/) is software for numeric optimization. PSL can use MOSEK as a conic program solver via a PSL add on.
Mosek support is provided as part of the [PSL Experimental](https://github.com/linqs/psl-experimental) package.

### Setting up the MOSEK add on

First, install MOSEK 6. In addition to a commercial version for which a 30-day trial is currently available, the makers of MOSEK also currently offer a free academic license. Users will need the "PTS" base system for using the linear distribution of the `ConicReasoner` and the "PTON" non-linear and conic extension to use the quadratic distribution. Both of these components are currently covered by the academic license.

After installing MOSEK, install the included `mosek.jar` file to your local Maven repository. (This file should be in `<mosek-root>/6/tools/platform/<your-platform>/bin`.)

```sh
mvn install:install-file -Dfile=<path-to-mosek.jar> -DgroupId=com.mosek \
    -DartifactId=mosek -Dversion=6.0 -Dpackaging=jar
```

Next, add the following dependency to your project's `pom.xml` file:
```xml
<dependencies>
    ...
    <dependency>
        <groupId>org.linqs</groupId>
        <artifactId>psl-mosek</artifactId>
        <version>YOUR-PSL-VERSION</version>
    </dependency>
    ...
</dependencies>
```

where `YOUR-PSL-VERSION` is replaced with your PSL version.

Finally, it might be necessary to rebuild your project.

### Using the MOSEK add on

After installing the MOSEK add on, you can use it where ever a `ConicProgramSolver` is used. To use it for inference with a `ConicReasoner` set the `conicreasoner.conicprogramsolver` [configuration](configuration.md) property to `oorg.linqs.psl.optimizer.conic.mosek.MOSEKFactory`.

Further, MOSEK requires that two environment variables be set when running. The same `bin` directory where you found `mosek.jar` needs to be on the path for shared libraries. The environment variable `MOSEKLM_LICENSE_FILE` needs to be set to the path to your license file (usually `<mosek-root>/6/licenses/mosek.lic`).

In bash in Linux, this can be done with the commands

```sh
export LD_LIBRARY_PATH=<path_to_mosek_installation>/mosek/6/tools/platform/<platform>/bin
export MOSEKLM_LICENSE_FILE=<path_to_mosek_installation>/mosek/6/licenses/mosek.lic
```

On Mac OS X, instead set ```DYLD_LIBRARY_PATH``` to the directory containing the MOSEK binaries.