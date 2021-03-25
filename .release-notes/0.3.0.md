## Exit successfully if there are no changes

This action now exits successfully if there are no changes to push. This can
happen when the action is run multiple times, for example when a failed workflow
is re-run. Previously, the action would exit with an error status on second run.

