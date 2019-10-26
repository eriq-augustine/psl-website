---
layout: wiki
---

### Setting up your environment
#### Cloning the PSL repository
If you are already comfortable using [Git](http://git-scm.com/) and you don't want or need to push commits to GitHub, then you can just clone the PSL repository using the command below. Otherwise, this [short primer](Using-Git.md) on some Git essentials may be useful.

```
>> git clone https://github.com/linqs/psl.git
```

### Building PSL from source
Change to the top-level directory of your working copy and run
```
>> mvn compile
```
You can install PSL to your local Maven repository by running
```
>> mvn install
```
## Best practices

## Git policies
If you're a member of the LINQS group, you may eventually need to release a new version of PSL. There are a number of steps involved in the process, which are detailed in the guide for [Releasing a New Stable Version](Releasing-a-New-Stable-Version.md). 


