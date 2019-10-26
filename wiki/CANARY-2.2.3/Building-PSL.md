---
layout: wiki
---

*This page is for building the PSL source code for the purposes of development.
For running a standard PSL program, see [Running a Program](Running-a-Program.md).*

To get the code, simply clone the repository:
```sh
git clone https://github.com/linqs/psl.git
```

If you plan on committing code or need the absolute latest, you may want to use the development repository:
```sh
git clone https://github.com/eriq-augustine/psl.git
```

If you are already comfortable using [Git](http://git-scm.com/), then you can just skip ahead to the section on compiling PSL.

### Getting started with Git

The [Git website](http://git-scm.com/) has information on installing Git, as does the GitHub guides mentioned below.
[This tutorial](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics) is helpful for learning how to use Git, and [this tutorial](https://git.wiki.kernel.org/index.php/GitSvnCrashCourse) is particularly helpful for SVN users.

Once Git is installed and you're ready to use it, you can run the above command to clone the PSL repository.

### Checking out the development branch

Between releases, the *develop* branch may be significantly ahead of the *master* branch.
To see the latest changes, checkout the *develop* branch.

```sh
git checkout develop
```

### Contributing Code

To contribute code to PSL first [fork](https://help.github.com/articles/fork-a-repo/) the [PSL development fork](https://github.com/eriq-augustine/psl).

Then you clone that repository to a local machine, make commits, and push some or all of those commits back to the repository on GitHub.
When your change is ready to be added to PSL, you can submit a [pull request](https://help.github.com/articles/about-pull-requests/) which will be reviewed by the PSL maintainers.
The maintainers may request that you make additional changes.
After your code is deemed acceptable, it will get merged into the *develop* branch of PSL.

### Building PSL

PSL uses the [maven build system](https://maven.apache.org/).
Move to the top-level directory of your working copy and run:
```sh
mvn compile
```

You can install PSL to your local Maven repository by running:
```sh
mvn install
```

### Updating your pom
Remember to update your project's `pom.xml` file with the (possibly) new version you installed.
