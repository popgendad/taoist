# taoist

Python-based command line interface for Todoist

[![Upload Python Package](https://github.com/popgendad/taoist/actions/workflows/python-publish.yml/badge.svg)](https://github.com/popgendad/taoist/actions/workflows/python-publish.yml)

This project is still under development and is not yet ready for release. It is a relatively simple utility that relies on the [official Todoist Python API](https://github.com/Doist/todoist-api-python).

The `taoist` utility has functionality for performing simple transactions involving both Todoist projects and tasks.

===

## Installation

The taoist package can be install via PyPi

```
pip install taoist
```

## Getting started

To connect `taoist` to your Todoist account, you must retrieve the API token. Once you have the API token, you
run

```
taoist init --token <TOKEN>
```

## Projects

The `taoist` utility currently has the functionality to perform the following project related transactions:

1. `list`: list user's projects
2. `create`: create a new user project
3. `delete`: delete an existing user project

## Tasks

The `taoist` utility can perform the following task-related transactions:

1. `list`: list user's tasks
2. `create`: create a new user task
3. `delete`: delete an existing user task
4. `edit`: edit properties of an existing user task
5. `move`: move an existing user task from one project to another
6. `tag`: add a tag to an existing user project
7. `done`: mark an existing user task as completed or done
