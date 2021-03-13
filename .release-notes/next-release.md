## Improve logging around multiple push attempts

Previously, if the bot failed to push its updates, it would create a log message for each pull that it attempted but only for the first push. This could be confusing to the user.

Now each push and pull attempt will be logged.

## Add support for updating `corral add` instructions in README.md

 The scope of the action-readme-version-updater has been expanded. Previously, it was focused not on updating our standard action READMEs. This change makes the action-readme-version-updater useful with our normal library READMEs that include instructions on how to use the library via corral. "Corral add" instructions can now include the proper current version.

