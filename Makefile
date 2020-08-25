TAG := docker.pkg.github.com/ponylang/action-readme-version-updater/action-readme-version-updater:latest

all: build

build:
	docker build --pull -t ${TAG} .

pylint: build
	docker run --entrypoint pylint --rm ${TAG} /entrypoint.py

.PHONY: build pylint
