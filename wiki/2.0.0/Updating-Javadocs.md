---
layout: wiki
---

We can use maven in the project root to create javadocs for all modules and link them together.
This applies to the primary `psl` repository, `psl-experimental`, and `psl-utils`.
```
mvn javadoc:aggregate
```

Note that `psl-experimental` and `psl-utils` depend on `psl`.
In addition, the javadocs for experimental and utils will try to link to psl.
So, the `psl` javadocs should be deployed before the experimental and util docs are built.