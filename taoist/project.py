"""project.py"""
import sys
import os
import argparse
from pathlib import Path
from configparser import ConfigParser
from todoist_api_python.api import TodoistAPI

def run_project(args: argparse.ArgumentParser) -> None:
    """
    Run project function
    """

    home_dir = Path.home()
    config_file = os.path.join(home_dir, ".taoist/config.ini")
    config = ConfigParser()
    if os.path.isfile(config_file):
        config.read(config_file)
    else:
        print("Error: Cannot read API token, please run init function")
        sys.exit(1)
    api = TodoistAPI(config['Default']['token'])
    if args.subcommand == "list":
        try:
            projects = api.get_projects()
        except Exception as error:
            print(error)
        for project in projects:
            print(project.id, "\t", project.name)
