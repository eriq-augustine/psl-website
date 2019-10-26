#!/usr/bin/env python3

import os
import shutil

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.join(THIS_DIR, '..')
TARGET_DIRS = [
    os.path.join(ROOT_DIR, 'api'),
    os.path.join(ROOT_DIR, 'wiki')
]

# The number of versions to keep unarchived.
VERSIONS_TO_KEEP = 2

MASTER_LABEL = 'master'
DEVELOP_LABEL = 'develop'

def processDir(targetDir):
    stableVersions = []
    devVersions = []

    for dirent in os.listdir(targetDir):
        path = os.path.join(targetDir, dirent)
        if (not os.path.isdir(path) or os.path.islink(path)):
            continue

        if (dirent.startswith('CANARY-')):
            devVersions.append(dirent)
        else:
            stableVersions.append(dirent)

    for (label, versions) in [(MASTER_LABEL, stableVersions), (DEVELOP_LABEL, devVersions)]:
        if (len(versions) == 0):
            continue

        versions = list(reversed(sorted(versions)))

        currentVersion = versions[0]
        newVersions = versions[:VERSIONS_TO_KEEP]
        oldVersions = versions[VERSIONS_TO_KEEP:]

        # Archive the old versions.
        for oldVersion in oldVersions:
            path = os.path.join(targetDir, oldVersion)

            shutil.make_archive(
                base_name = path,
                format = 'zip',
                root_dir = targetDir,
                base_dir = oldVersion
            )

            shutil.rmtree(path)

        # Mark the newest version with the label.
        link = os.path.join(targetDir, label)

        if (os.path.islink(link)):
            os.unlink(link)

        # Note that we want the link relative.
        os.symlink(currentVersion, link)

def main():
    for targetDir in TARGET_DIRS:
        processDir(targetDir)

if (__name__ == '__main__'):
    main()
