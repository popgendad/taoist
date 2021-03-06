<img src="docs/source/images/taijitu.png" width="100" />

# Taoist: Python-based Terminal Utility for Todoist

[![Upload Python Package](https://github.com/popgendad/taoist/actions/workflows/python-publish.yml/badge.svg)](https://github.com/popgendad/taoist/actions/workflows/python-publish.yml)
[![Documentation Status](https://readthedocs.org/projects/taoist/badge/?version=latest)](https://taoist.readthedocs.io/en/latest/?badge=latest)
      

This project is still under development and is not yet ready for release. It is a simple utility that relies on the [official Todoist Python REST API](https://github.com/Doist/todoist-api-python). This software is not created by, affiliated with, or supported by Doist. The `taoist` utility has functionality for performing basic transactions involving Todoist projects, sections, labels and tasks. The goal of the project is to enable most major components of 
a ["getting-things-done"](https://todoist.com/productivity-methods/getting-things-done) workflow from a terminal environment and is not intended to replicate the functionality of the Todoist app.

## Quick Start

 The taoist package can be installed via PyPi
 ```
 $ pip3 install taoist
 ```
 Next, connect `taoist` to your Todoist account. First you must retrieve your API token from the Todoist app.
 Once you have your API token, you can authenticate to the web service by running
 ```
 taoist init --token <TOKEN>
 ```
 if run without the `--token` switch, you will be interactively prompted to provide the API token.

 To see your list of projects, run
 ```
 taoist project list
 ```
 Similarly, to see your list of tasks, run
 ```
 taoist task list
 ```

## Documentation

Please visit [readthedocs](https://taoist.readthedocs.io/en/latest) for full documentation of the `taoist` project
