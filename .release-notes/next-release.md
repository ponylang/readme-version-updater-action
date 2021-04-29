## Fix build error coming from PyGitHub dependency

With the release of a new version of PyGitHub, the pynacl dependency changed and no longer builds. We are fine using the previous version of PyGitHub so this update pins us to that version. If we need to upgrade in the future, we'll need to fix the "can't build pynacl" issue.

## Add support for updating "docker style" use actions

With GitHub actions, in addition to actions that are built on each run, you can also use a form that starts with `docker://` to load a prebuilt image DockerHub. Previously, this form of README update wasn't supported.

We now support updating `docker://` links to DockerHub. In particular, the following format is now supported:

```
docker://github/super-linter:v3.8.3
```

