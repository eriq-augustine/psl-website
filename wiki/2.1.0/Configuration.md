---
layout: wiki
---

See the [Configuration Options](Configuration-Options.md) page for all options that PSL uses.

Many components of the PSL software have modifiable parameters and options, called properties.
Every property has a key, which is a string that uniquely identifies it. 
These keys are organized into a namespace hierarchy, with each level separated by dots, e.g. `<namespace>.<option>`.

Each PSL class can specify a namespace for the options used by the class and its subclasses.
For example, the `org.linqs.psl.application.learning.weight.VotedPerceptron` weight learning class uses the namespace `votedperceptron`.
Setting the configuration option `votedperceptron.stepsize` allows you to control the size of the gradient descent update step in the `VotedPerceptron` weight learning class.

Every property has a type and a default value, which is the value the object will use unless a user overrides it. 
Every class with properties documents them by declaring their keys as public static final Strings, with Javadoc comments describing the corresponding property's type and semantics.
Another public static final member declares the default value for that property.

## Setting Properties

Setting properties for PSL programs differ depending on whether you are using the CLI or Java/Groovy interface.

### CLI
CLI users can pass any PSL configuration property on the CLI command line.
Just use the `-D` option and specify the key-value pair.
For example, you can run PSL with debug logging like this:
```sh
java -jar psl.jar --infer --data example.data --model example.psl -D log4j.threshold=DEBUG
```

### Java/Groovy
PSL projects can specify different configuration bundles in a file named `psl.properties` on the classpath.
The standard location for this file is `<project root>/src/main/resources/psl.properties`.
Each key-value pair should be specified on its own line with a `<namespace>.<option> = <value>` format.

Here is an example `psl.properties`:
```ini
# This is an example properties file for PSL.
# 
# Options are specified in a namespace hierarchy, with levels separated by '.'.

# Weight learning parameters

# This property specifies the number of iterations of voted perceptron updates
votedperceptron.numsteps = 700

# This property specifies the initial step size of the voted perceptron updates
votedperceptron.stepsize = 0.1
```

## Getting Properties

Properties can only be fetched from a running program in the Java/Groovy interface.
They are accessed statically via the `org.linqs.psl.config.Config` class.

For example:
```java
import org.linqs.psl.config.Config;

public static void main(String[] args) {
   System.out.println(Config.getString("key", "default"));
}
```
