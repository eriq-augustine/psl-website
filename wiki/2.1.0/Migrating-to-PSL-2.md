---
layout: wiki
---

## Maven Repository Move
Our Maven repository has moved
 - from: `https://scm.umiacs.umd.edu/maven/lccd/content/repositories/psl-releases/`
 - to: `http://maven.linqs.org/maven/repositories/psl-releases/`

The new endpoint will redirect to a https endpoint that may be used if necessary:
`https://linqs-data.soe.ucsc.edu/maven/repositories/psl-releases/`

## Naming Changes

### Package Renames
All packages have been renamed from `edu.umd.cs.*` to `org.linqs.*`.

### Renames/Moves
 - `edu.umd.cs.psl.model.argument.ArgumentType` → `org.linqs.psl.model.term.ConstantType`

## Usage Changes

### Predicate Arguments
`ArgumentType.*` → `ConstantType.*`  
The arguments for a predicate are now defined in `org.linqs.psl.model.term.ConstantType` instead of `edu.umd.cs.psl.model.argument.ArgumentType`.
All the same types are supported, just the containing class has been moved and renamed.

### Getting a Partition
`new Partition(int)` → `DataStore.getPartition("stringIdentifier")`  
If the partition does not exist, it will be created and returned.
If it exists, it will be returned.
It is not longer necessary to pass around partitions if you don't want to.

### Changes to Rule Syntax
Arithmetic rules are now supported in 2.0.
See the [Rule Specification](Rule-Specification.md) for details.
Rules in Groovy can now be specified in additional ways. See [Rule Specification in Groovy](Rule-Specification-in-Groovy.md).

### Constraints
Constraints are now implemented using unweighted arithmetic rules.
See [Constraints](Constraints.md) for more details.

## Util and Experimental Breakout
To speed up utility development and reduce bloat, some components have been removed from this primary PSL repository and brought into their own repositories.
In these sample POM snippets all versions have been set to `CANARY`, however you may choose your corresponding release.

### PSL Utils
https://github.com/linqs/psl-utils

#### Data Loading - `psl-dataloading`

##### Maven Dependency Declaration
```
<dependency>
  <groupId>org.linqs</groupId>
  <artifactId>psl-dataloading</artifactId>
  <version>CANARY</version> 
</dependency>
```

##### Included (Old) Packages
 - `edu.umd.cs.psl.ui.loading`
 - `edu.umd.cs.psl.ui.data`

##### New Package
 - `org.linqs.psl.utils.dataloading`

___

#### Evaluation - `psl-evaluation`
```
<dependency>
  <groupId>org.linqs</groupId>
  <artifactId>psl-evaluation</artifactId>
  <version>CANARY</version> 
</dependency>
```

##### Included (Old) Packages
 - `edu.umd.cs.psl.evaluation`

##### New Package
 - `org.linqs.psl.utils.evaluation`

___

#### Text Similarity - `psl-textsim`
```
<dependency>
  <groupId>org.linqs</groupId>
  <artifactId>psl-textsim</artifactId>
  <version>CANARY</version> 
</dependency>
```

##### Included (Old) Packages
 - `edu.umd.cs.psl.ui.functions.textsimilarity`

##### New Package
 - `org.linqs.psl.utils.textsimilarity`

___

### PSL Experimental
https://github.com/linqs/psl-experimental

#### Data Splitter - `psl-datasplitter`
```
<dependency>
  <groupId>org.linqs</groupId>
  <artifactId>psl-datasplitter</artifactId>
  <version>CANARY</version> 
</dependency>
```

##### Included (Old) Packages
 - `edu.umd.cs.psl.util.datasplitter`

##### New Package
 - `org.linqs.psl.experimental.datasplitter`

___

#### Experiment - `psl-experiment`
```
<dependency>
  <groupId>org.linqs</groupId>
  <artifactId>psl-experiment</artifactId>
  <version>CANARY</version> 
</dependency>
```

##### Included (Old) Packages
 - `edu.umd.cs.psl.ui.experiment`

##### New Package
 - `org.linqs.psl.experimental.experiment`

___

#### Mosek - `psl-mosek`
```
<dependency>
  <groupId>org.linqs</groupId>
  <artifactId>psl-mosek</artifactId>
  <version>CANARY</version> 
</dependency>
```

##### Included (Old) Packages
 - `edu.umd.cs.psl.optimizer.conic.mosek`

##### New Package
 - `org.linqs.psl.optimizer.conic.mosek`

___

#### Optimize - `psl-optimize`
```
<dependency>
  <groupId>org.linqs</groupId>
  <artifactId>psl-optimize</artifactId>
  <version>CANARY</version> 
</dependency>
```

##### Included (Old) Packages
 - `edu.umd.cs.psl.optimizer`
 - `edu.umd.cs.psl.reasoner.conic`

##### New Package
 - `org.linqs.psl.experimental.optimizer`

___

#### Sampler - `psl-sampler`
```
<dependency>
  <groupId>org.linqs</groupId>
  <artifactId>psl-sampler</artifactId>
  <version>CANARY</version> 
</dependency>
```

##### Included (Old) Packages
 - `edu.umd.cs.psl.sampler`

##### New Package
 - `org.linqs.psl.experimental.sampler`

___

#### Weight Learning - `psl-weightlearning`
```
<dependency>
  <groupId>org.linqs</groupId>
  <artifactId>psl-weightlearning</artifactId>
  <version>CANARY</version> 
</dependency>
```

##### Included (Old) Packages
 - `edu.umd.cs.psl.application.learning.weight.maxmargin`

##### New Package
 - `org.linqs.psl.experimental.learning.weight.maxmargin`