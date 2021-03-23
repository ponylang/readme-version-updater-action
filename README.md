# README Version Updater

Updates version info in a project's README on release. This action assumes that you are using our [release-bot-action](https://github.com/ponylang/release-bot-action) to do releases.

Two different possible version types are currently updated:

- Action usage instructions

For example, this README contains `ponylang/readme-version-updater-action@0.2.0` within the example workflow below. On release, that will be updated to whatever the new version is.

- Corral add instructions

It's a common pattern for a Pony library's README to include information on how
to add the library to a project using `corral add`. For example:

```text
corral add github.com/ponylang/appdirs.git --version 0.1.0
```

On release of said library, the version in the corral add string will be updated by this action to whatever the new version is. Note that because this action is a GitHub action, corral add instruction updating only works for add instructions that are referencing a git repo.

A project's README is assumed to be named either `README.md` or `README.rst`. The first one found will be used. The action will fail if no README file is found.

## Example workflow

The readme-version-updater-action should be set up as an "artefact building step" in the release-bot-action's [release.yml](https://github.com/ponylang/release-bot-action#trigger-release-announcement).

```yml
name: Release

on:
  push:
    tags:
      - \d+.\d+.\d+

jobs:
  update-version-in-readme-examples:
    runs-on: ubuntu-latest
    name: Update version in README examples
    steps:
      - name: Update version in README examples
        uses: ponylang/readme-version-updater-action@0.2.0
        with:
          git_user_name: "Ponylang Main Bot"
          git_user_email: "ponylang.main@gmail.com"
        env:
          API_CREDENTIALS: ${{ secrets.GITHUB_TOKEN }}
```

Note, you do not need to create `GITHUB_TOKEN`. It is already provided by GitHub. You merely need to make it available to the readme-version-updater-action action.
