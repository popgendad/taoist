"""project.py"""
import sys
import os
import argparse
from tabulate import tabulate
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
        project_list = [["id", "name"],]
        try:
            projects = api.get_projects()
        except Exception as error:
            print(error)
        for project in projects:
            row = [project.id, project.name]
            project_list.append(row)
        print(tabulate(project_list, headers="firstrow"))
    elif args.subcommand == "create":
        try:
            project = api.add_project(name=args.name)
        except Exception as error:
            print(error)
    elif args.subcommand == "delete":
        try:
            is_success = api.delete_project(project_id=int(args.id))
        except Exception as error:
            print(error)        
