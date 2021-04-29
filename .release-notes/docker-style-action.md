## Add support for updating "docker style" use actions

With GitHub actions, in addition to actions that are built on each run, you can also use a form that starts with `docker://` to load a prebuilt image DockerHub. Previously, this form of README update wasn't supported.

We now support updating `docker://` links to DockerHub. In particular, the following format is now supported:

```
docker://github/super-linter:v3.8.3
```
