#!/usr/bin/python3

import git,json,os,re,sys
from github import Github

ENDC   = '\033[0m'
ERROR  = '\033[31m'
INFO   = '\033[34m'
NOTICE = '\033[33m'

if not 'API_CREDENTIALS' in os.environ:
  print(ERROR + "API_CREDENTIALS needs to be set in env. Exiting." + ENDC)
  sys.exit(1)

# Get repository and version names from the environment
# version is in the form of "refs/tags/1.0.0" where the version is 1.0.0
repository = os.environ['GITHUB_REPOSITORY']
version = re.sub('refs/tags/', '', os.environ['GITHUB_REF'])

# login
github = Github(os.environ['API_CREDENTIALS'])

print(INFO + "Cloning repo." + ENDC)
clone_from = "https://" + os.environ['GITHUB_ACTOR'] + ":" + os.environ['API_CREDENTIALS'] + "@github.com/" + repository
git = git.Repo.clone_from(clone_from, '.').git

print(INFO + "Setting up git configuration." + ENDC)
git.config('--global', 'user.name', os.environ['INPUT_GIT_USER_NAME'])
git.config('--global', 'user.email', os.environ['INPUT_GIT_USER_EMAIL'])

# what to find and what to replace it with
find = f'{repository}@\d+\.\d+\.\d+'
replace = f'{repository}@{version}'

# open README.md and update with new version
print(INFO + "Updating version to " + replace + ENDC)
readme = open("README.md", "r+")
text = readme.read()
text = re.sub(find, replace, text)
readme.seek(0)
readme.write(text)
readme.close()

print(INFO + "Adding git changes." + ENDC)
git.add('README.md')
git.commit('-m', f'Update README examples to reflect new version {version}')

print(INFO + "Pushing updated README." + ENDC)
push_failures = 0
while(True):
  try:
    git.push()
    break
  except:
    push_failures += 1
    if (push_failures <= 5):
      print(NOTICE + "Failed to push. Going to pull and try again." + ENDC)
      git.pull()
    else:
      print(ERROR + "Failed to push again. Giving up." + ENDC)
      raise
