---
layout: wiki
---

This is a HOWTO on changing the version number in the PSL code base. In most, if not all, cases, this HOWTO should be followed as part of a larger one, such as [Releasing a New Stable Version](Releasing-a-New-Stable-Version.md), not by itself.

# Version Number Policy

A new version number should be applied as a new commit that does nothing else, so make sure you are working on a clean working copy with no uncommitted changes.

Version numbers consist of the following components:

* x = major version
* y = minor version
* z = patch version

Your new version number should be of the form x.y.z (for a stable version) or x.y.z-SNAPSHOT (for an unstable version).

All the occurrences of a PSL version number should be kept in sync, i.e., have the same value for all occurrences in all `pom.xml` files and other resources across all modules. In addition, **only one commit in the entire Git repository should have a particular stable version number**.

# Edit the code

Each `pom.xml` has **only one** instance of the version number that will need to be changed.
You can change each instance manually, or use the following commands (replacing `2.0.0-SNAPSHOT` and `2.1.0-SNAPSHOT` with the actual versions):
```sh
find . -name pom.xml | xargs grep '<version>2.0.0-SNAPSHOT</version>' # Examine the results and ensure that you are only updating correct references.
find . -name pom.xml | xargs sed -i 's#<version>2.0.0-SNAPSHOT</version>#<version>2.1.0-SNAPSHOT</version>#g' # Perform the actual replacement.
```

# Commit

Commit the changes with one of the following commit messages.

If you are changing to a stable version, use:
```
Version x.y.z
```

If you are changing to a new snapshot version, use:
```
Started x.y.z-SNAPSHOT
```

Push your commit when finished.