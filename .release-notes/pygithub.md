## Fix build error coming from PyGitHub dependency

With the release of a new version of PyGitHub, the pynacl dependency changed and no longer builds. We are fine using the previous version of PyGitHub so this update pins us to that version. If we need to upgrade in the future, we'll need to fix the "can't build pynacl" issue.
