---
layout: wiki
---

The PSL software uses concepts from the [PSL paper](http://arxiv.org/abs/1505.04406.md), and introduces new ones for advanced data management and machine learning. On this page, we define the commonly used terms and point out the corresponding classes in the codebase.

Please note that this page is organized conceptually, not alphabetically.

## Preliminaries

**Hinge-loss Markov random field:** A factor graph defined over _continuous_ variables in the [0,1] interval with (log) factors that are hinge-loss functions. Many classes in PSL work together to implement the functionality of HL-MRFs, but the class for storing collections of hinge-loss potentials, which define HL-MRFs, is [GroundRuleStore.java](https://github.com/linqs/psl/blob/master/psl-core/src/main/java/org/linqs/psl/application/groundrulestore/GroundRuleStore.java.md).

**Ground atom:** A logical relationship corresponding to a random variable in a HL-MRF. For example, `Friends("Steve", "Jay")` is an alias for a specific random variable. Implemented in [GroundAtom.java](https://github.com/linqs/psl/blob/master/psl-core/src/main/java/org/linqs/psl/model/atom/GroundAtom.java.md).

**Random variable atom:** A ground atom that is unobserved, i.e., no value is known for it. A HL-MRF assigns probability densities to assignments to random variable atoms. Implemented in [RandomVariableAtom.java](https://github.com/linqs/psl/blob/master/psl-core/src/main/java/org/linqs/psl/model/atom/RandomVariableAtom.java.md).

**Observed atom:** A ground atom that has an observed, immutable value. HL-MRFs are conditioned on observed atoms. Implemented in [ObservedAtom.java](https://github.com/linqs/psl/blob/master/psl-core/src/main/java/org/linqs/psl/model/atom/ObservedAtom.java.md).

**Atom:** A generalization of ground atoms that allow logical variables as placeholders for constant arguments. For example, `Friends("Steve", A)` is a placeholder for all the ground atoms that can be obtained by substituting constants for the logical variable `A`. Implemented in [Atom.java](https://github.com/linqs/psl/blob/master/psl-core/src/main/java/org/linqs/psl/model/atom/Atom.java.md).

## Syntax

**PSL Program:** A set of rules, each of which is a template for hinge-loss potentials or hard linear constraints. When grounded over a base of ground atoms, a PSL program induces a HL-MRF conditioned on any specified observations. Implemented in [Model.java](https://github.com/linqs/psl/blob/master/psl-core/src/main/java/org/linqs/psl/model/Model.java.md).

**Rule:** See [Rule Specification](Rule-Specification.md).

## Data Management

**Data Store:** An entire data repository, such as a relational database management system (RDBMS). Implemented in [DataStore.java](https://github.com/linqs/psl/blob/master/psl-core/src/main/java/org/linqs/psl/database/DataStore.java.md).

**Partition:** A logical division of ground atoms in a data store. Implemented in [Partition.java](https://github.com/linqs/psl/blob/master/psl-core/src/main/java/org/linqs/psl/database/Partition.java.md).

**Database:** A logical view of a data store, constructed by specifying a write partition and one or more read partitions of a data store. Implemented in [Database.java](https://github.com/linqs/psl/blob/master/psl-core/src/main/java/org/linqs/psl/database/Database.java.md).

**Open Predicate:** A predicate whose atoms can be random variable atoms, i.e., unobserved.The only time a ground atom will be loaded as a random variable atom is when it is stored in the database's write partition and its predicate is _not_ specified as closed. Otherwise it will be loaded as an observed atom. Whether a predicate is open or closed is specific to each database.

**Closed Predicate:** A predicate whose atoms are always observed atoms. The only time a ground atom will be loaded as a random variable atom is when it is stored in the database's write partition and its predicate is _not_ specified as closed. Otherwise it will be loaded as an observed atom. Whether a predicate is open or closed is specific to each database.