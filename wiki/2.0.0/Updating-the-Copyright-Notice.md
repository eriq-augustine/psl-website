---
layout: wiki
---

Before [releasing a new stable version](releasing-a-new-stable-version.md), it is good to make sure that PSL's copyright notices are up to date. This can be simply done from the command line.

For example, if I wanted to update the copyright from `2013-2015` to `2013-2017`, I could do the following in the project root:

```sh
mvn clean  # We do not want to bother updating any compiled artifacts.
grep -R "2013-2015"  # Examine the results and ensure that you are only updating correct references.
grep -Rl "2013-2015" | xargs sed -i 's/2013-2015/2013-2017/g'  # Do the actual replacement.
```