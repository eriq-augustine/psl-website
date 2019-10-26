---
layout: wiki
---

The `.data` files for the PSL CLi are [YAML](https://en.wikipedia.org/wiki/YAML) files with some additional constraints.

The accepted top-level keys for data files are:
 - `predicates`
 - `observations`
 - `targets`
 - `truth`

### predicates

This section defines the allowed predicates for a PSL program.
The minimum amount of information that must be supplied for a predicate is:
 - Name
 - Arity (how many arguments the predicate has)
 - Whether the predicate is `open` or `closed`.

A simple `predicates` section may look like:
```
predicates:
   Foo/2: closed
   Bar/2: open
```

In addition to the base information, you can also specify the types of the predicate arguments and whether or not the predicate is a block.
These are specified with the `types` and `block` keys respectively.
If the types of a predicate are not explicitly stated, then `UniqueStringID` is used (or `UniqueIntID` if `--int-ids` is specified as a command line option).
If an arity is not specified, then the number of supplied types is inferred to be the arity.
If both the arity and specific types are supplied, then both sizes much match.
Allowed types are specified by the [ConstantType](https://linqs-data.soe.ucsc.edu/psl-docs/docs/psl/develop-head/org/linqs/psl/model/term/ConstantType.html) enum.
The blocking nature of a predicate is used in some advanced and experimental PSL features.

A more advanced `predicates` section may look like:
```
predicates:
   Foo/2:
      - closed
      - types:
         - UniqueIntID
         - String
   Bar:
      - open
      - types:
         - UniqueStringID
         - Integer
      - block
```

### Partitions

The remaining top level keys are all partitions that data should be loaded into:
 - `observations`
 - `targets`
 - `truth`

In these sections, you specify the files that should be loaded into each partition for each predicate.
One or more tab-separated files may be specified for each partition and predicate.
If you do not have data for a predicate/partition pairing, just leave it out.

Below is a sample of these sections:
```
observations:
   Foo: foo_obs.txt
   Bar: bar_obs.txt

targets:
   Foo:
      - foo_targets_1.txt
      - foo_targets_2.txt

truth:
   Foo: foo_truth.txt
```