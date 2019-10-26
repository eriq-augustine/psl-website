---
layout: wiki
---

Version 2.1.0 (https://github.com/linqs/psl/tree/2.1.0)  
[Full Change Information](https://psl.linqs.org/blog/2018/07/30/psl-2.1.0-release.html)

   - PostgreSQL Database Backend
   - Removed MySQL support
   - Removed the Queries Class
   - Removed InserterUtils
   - Bulk Dataloading in Postgres
   - Deferred Indexing
   - No More Predicate Deserialization
   - UniqueID Storage Types
   - Long Predicate Names Allowed
   - CLI Configuration Properties
   - Complete CLI Predicate Typing
   - Getting the PSL Version
   - Random in PSL
   - Parallelization in PSL
   - Configuration Reworked
   - New Canary Naming System
   - Inference API Rework
   - Moved PSL Evaluation
   - Evaluation Infrastructure Changes
   - External Function Support

Version 2.0.0 (https://github.com/linqs/psl/tree/2.0.0)
   - Add a new type of rule called [Arithmetic Rules](Rule-Specification.md#arithmetic-rules).
      - The use case previously satisfied by [Constraints](Constraints.md) have been replaced by arithmetic rules.
   - The [Rule Syntax](Rule-Specification.md) has been expanded to accomodate arithmetic rules.
      - Rules in Groovy may now be specified [using strings](Rule-Specification-in-Groovy.md#string-syntax).
      - Rules in Groovy may now be specified [in bulk](Rule-Specification-in-Groovy.md#bulk-string-syntax) using large strings or files.
   - A [CLI Interface](Using-the-CLI.md) has been added to PSL to help develop program more quickly.
   - All PSL packages [have been renamed](Migrating-to-PSL-2.md#naming-changes) from `edu.umd.cs` to `org.linqs`.
   - [PSL Examples](Examples.md) have been relocated to an [external repository](https://bitbucket.org/linqs/psl-examples) instead of a maven archetype.
   - Many non-critical components [have been moved out](Migrating-to-PSL-2.md#util-and-experimental-breakout) to two external repositories:
      - [PSL Utils](https://github.com/linqs/psl-utils)
      - [PSL Experimental](https://github.com/linqs/psl-experimental)
   - The PSL [Maven Repository](Migrating-to-PSL-2.md#maven-repository-move) has been moved.
   - Bug fixes.
   - Performances Enhancements.

Version 1.2.1 (https://github.com/linqs/psl/tree/1.2.1)
* Bug fix for External Function registration 

Version 1.2 (https://github.com/linqs/psl/tree/1.2)

* Expectation-maximization and [paired-dual learning] (http://linqs.cs.umd.edu/basilic/web/Publications/2015/bach:icml15/bach-icml15.pdf) in the org.linqs.psl.application.learning.weight.em package
* Topic modeling with [latent topic networks](http://linqs.cs.umd.edu/basilic/web/Publications/2015/foulds:icml15/Foulds2015LatentTopicNetworks.pdf) in the org.linqs.psl.application.topicmodel package
* Support for [averaging rules](http://www.cs.utexas.edu/users/ml/papers/beltagy.acl14.pdf) in the org.linqs.psl.model.kernel.rule package
* New DateTime and Long attribute types in the org.linqs.psl.model.argument package, thanks to Jack Sullivan
* Java 8 compatibility
* Support for MySQL backend (except for external functions)
* Bug fixes

Version 1.1.1 (https://github.com/linqs/psl/tree/1.1.1)

* Improved examples, which demonstrate database population for non-lazy inference and learning
* Support for learning negative weights (limited to inference methods for discrete MRFs that support negative weights)
* Bug fixes

Version 1.1 (https://github.com/linqs/psl/tree/1.1)

* An improved Groovy interface. Try the new examples via https://github.com/linqs/psl/wiki/Installing-examples to learn the new interface.
* New, improved psl-core architecture
* Much faster inference based on the alternating direction method of multipliers (ADMM).
* Improved max-likelihood weight learning
* New max-pseudolikelihood and large-margin weight learning
* Many bug fixes and minor improvements.

Version 1.0.2 (https://github.com/linqs/psl/tree/1.0.2)

* Fixed bugs in HomogeneousIPM and MOSEK add-on caused by bug in parallel colt when using selections from large, sparse matrices.
* Fixed bug when learning weights of programs which contain set functions.
* Reduced memory footprint of HomogeneousIPM and matrices produced by ConicProgram.

Version 1.0.1 (https://github.com/linqs/psl/tree/1.0.1)

* Fixed bug in optimization program when the same atom was used more than once in a ground rule or constraint.
* Added release profile to parent POM for better packaging.
* Minor changes to archetypes.

Version 1.0 (https://github.com/linqs/psl/tree/1.0)