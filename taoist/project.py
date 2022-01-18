"""project.py"""
import argparse
from taoist.read_config import read_config
from tabulate import tabulate
from todoist_api_python.api import TodoistAPI

def run_project(args: argparse.ArgumentParser) -> None:
    """
    Run project function
    """

    # Read taoist user configuration
    config = read_config()

    # Initialize Todoist API
    api = TodoistAPI(config['Default']['token'])

    # Process subcommand
    if args.subcommand == "list":
        table_header = ["id", "name"]
        project_list = [table_header,]
        try:
            projects = api.get_projects()
        except Exception as error:
            print(error)
        for project in projects:
            row = [project.id, project.name]
            project_list.append(row)
        
        # Print project list table
        print(tabulate(project_list, headers="firstrow"))
    elif args.subcommand == "create":
        try:
            project = api.add_project(name=args.project_name)
        except Exception as error:
            print(error)
    elif args.subcommand == "delete":
        try:
            is_success = api.delete_project(project_id=args.project_id)
        except Exception as error:
            print(error)        
