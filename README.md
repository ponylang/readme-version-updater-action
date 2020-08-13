# Action README Version Updater

Updates the version of an action in its README on release. This action assumes that you are using our [release-bot-action](https://github.com/ponylang/release-bot-action) to do releases.

For example, this README contains `ponylang/action-readme-version-updater@0.0.0` within the example workflow below. On release, that will be updated to whatever the new version is and that change will be pushed back to the repo as part of the "artefact building steps" that you include as part of setting up the release-bot-action.

## Example workflow

The action-readme-version-updater should be set up as an "artefact building step" in the release-bot-action's [release.yml](https://github.com/ponylang/release-bot-action#trigger-release-announcement).

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
        uses: ponylang/action-readme-version-updater@0.0.1
        with:
          git_user_name: "Ponylang Main Bot"
          git_user_email: "ponylang.main@gmail.com"
        env:
          API_CREDENTIALS: ${{ secrets.GITHUB_TOKEN }}
```

Note, you do not need to create `GITHUB_TOKEN`. It is already provided by GitHub. You merely need to make it available to the action-readme-version-updater action.
