---
layout: wiki
---

This a HOWTO on releasing a new stable PSL version. All first and second level headers are steps in the process, and should be followed sequentially.

# Preliminaries

## Get the Code Ready
A release is a single commit that increments the software's version number to a stable version number and does nothing else. So, before you release a version, make sure all your changes are committed and pushed, and the code is in the state in which you want to release it. 

Make sure the [copyright notices](Updating-the-Copyright-Notice.md) are up to date.

## Test the Code
Remember to test the code and double check it is ready for release.
To clean, compile, and test the code, you can do:
```
mvn clean test
```

## Find the New Version Number
Stable version numbers are of the format x.y.z, where

* x = major version
* y = minor version
* z = patch version

The git branch the code is on (the working branch) should already have a version number in its `pom.xml` files of the form x.y.z-SNAPSHOT. Whatever x.y.z-SNAPSHOT is, the new version will be x.y.z.

# Create the Stable Release

## Change the Version
The first step is to [change the version number](Updating-the-version-number.md) to the stable version number. Remember to perform the commit at the end of the instructions.

## Tag the New Stable Version
Run the following two commands:
```sh
git tag -a x.y.z -m 'Version x.y.z'
git push origin x.y.z
```

# Update Git Branches

There are two ways the branch structure of the Git repo can change because of a new stable version:

1. The master branch might need to be updated
1. The working branch might need to be deleted

## Updating the Master Branch

The Master branch should always point to the commit of the highest stable version number, where x, y, and z are treated as separate orders of magnitude.

So, if the master branch points to version 1.2, then releasing 1.1.1 would not update the master branch, but releasing 1.2.1 or 1.3 would.

If you are updating the master branch, it should already be upstream of the new stable version. Substituting the working branch name for WORKING_BRANCH, simply run the following commands:

```sh
git checkout master
git pull origin WORKING_BRANCH
git push
```

## Deleting the working branch

There should now be a working branch pointing to the tag "x.y.z" (and possibly the master branch). If the working branch is not the develop branch, it should probably be deleted (which deletes the branch name, not the commit itself). Don't delete the develop branch! Substituting the working branch name for WORKING_BRANCH, run the following commands:
```sh
git branch -d WORKING_BRANCH
git push origin :WORKING_BRANCH
```

# Deploy New Stable Version

With the new stable version checked out, on a machine with file system access to the repository, in the top level directory of the project (the one with the PSL project pom.xml file, not any of the subprojects), run the following commands:
```sh
mvn clean
mvn deploy
```

# Last Steps

## Update Change Log

Update the [change log](change-log.md) with a list of the main changes since the most recent upstream stable version. For example, if releasing 1.0.2, list the main changes since 1.0.1, even if there is a more recent 1.1 release.

## Announce New Release

Post an announcement on the [user group](https://groups.google.com/forum/.md#!forum/psl-users). Remember to select the "make an announcement" option, rather than "start a discussion." Here is a template:

```
Subject: New Version: x.y.z

A new stable version of PSL, version x.y.z (https://github.com/linqs/psl/tree/x.y.z) is now available.

See [switching the PSL version your program uses](switching-the-PSL-version-your-program-uses.md) for instructions on changing your PSL projects to the new version.

In version x.y.z:
[A list of the main changes]
```
