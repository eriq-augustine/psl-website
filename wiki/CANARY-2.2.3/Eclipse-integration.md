---
layout: wiki
---

Since PSL is built with Java and Maven, many IDEs are supported.
(Although many PSL developers prefer using vim/emacs and a terminal.)
One of the popular supported IDEs is Eclipse.

[Eclipse](http://www.eclipse.org) is an extensible, integrated development environment that can be used to develop PSL and PSL projects.
The recommended way of using Eclipse with PSL is to use the [Eclipse plugin for Maven](http://maven.apache.org/plugins/maven-eclipse-plugin/) to generate Eclipse project information for a PSL project and then import that project into Eclipse.

### Prerequisites
Ensure that you have version 3.6 (Helios) or higher of Eclipse installed.
Then, install the [Groovy Eclipse plugin](https://github.com/groovy/groovy-eclipse/wiki#how-to-install) and the optional 1.8 version of the Groovy compiler, which is available when installing the plugin.
The version 1.8 compiler is what [Maven will use](https://github.com/groovy/groovy-eclipse/wiki/Groovy-Eclipse-Maven-plugin) to compile the Groovy scripts, so builds done by either tool should be interchangeable.
If you use an older version, Eclipse will probably recompile some files which then won't be compatible with the rest, and it won't run. (Cleaning and rebuilding everything should help.)

You might have to change the Groovy compiler version to 1.8.x in your Groovy compiler preferences (part of the Eclipse preferences).

You need to add a classpath variable in Eclipse to point to your local Maven repository.
You can access the variables either from the main options or from the build-path editor for any project.
Where you specify additional libs, make a new variable (there should be a button) with the name `M2_REPO` and the path to your repo (e.g., `~/.m2/repository`).
This can also be achieved automatically via the following Maven command:
```sh
mvn -Declipse.workspace=/path/to/workspace eclipse:configure-workspace
```

### Generating and importing Eclipse metadata
In the top-level directory of your PSL project, run:
```sh
mvn eclipse:eclipse
```

Then in Eclipse, go to `File/Import/General/\<something like 'Existing Project'\>`.
Select the top-level directory of your project.
You probably don't want to copy it into the workspace, so uncheck that option.

### Running programs ###
Be sure to run as a "Java application."

**Tips**

If you want to delete the Eclipse metadata for any reason, run:
```
mvn eclipse:clean
```

If you want to generate metadata for a project that depends on another project you're developing with Eclipse (PSL or not), run:
```
mvn eclipse:eclipse -Declipse.workspace=<path to Eclipse workspace>
```

The Eclipse plugin for Maven will look in the provided workspace for any projects that match dependencies declared in your project's POM file.
Your project will be configured to depend on any such projects found as opposed to their respective installed jars.
This way, changes to the sources of those dependencies will be seen by your project without reinstalling the dependencies. Note that this works even for dependencies that were imported but not copied into the workspace.

The [m2eclipse Eclipse plugin](http://www.eclipse.org/m2e/) is another option for developing PSL projects with Eclipse.
It differs from the recommended method in that it is an Eclipse plugin designed to support Maven projects, as opposed to a Maven plugin designed to support Eclipse.
