"""task.py"""
import json
from argparse import ArgumentParser
from taoist.read_project_dict import read_project_dict
from tabulate import tabulate
from todoist_api_python.api import TodoistAPI

def run_task(args: ArgumentParser) -> None:
    """
    Run the task command
    """

    # Read config and project list
    config, project_dict = read_project_dict()

    # Initialize Todoist API
    api = TodoistAPI(config['Default']['token'])

    # Get tasks
    tasks = api.get_tasks()

    # Process subcommand
    if args.subcommand == "list":
        task_list = [["id", "content", "project", "status", "due"],]
        for task in tasks:
            status = "Open"
            if task.completed:
                status = "Done"
            row = [task.id, task.content, project_dict[task.project_id].name, status, task.due.date]
            task_list.append(row)
        print(tabulate(task_list, headers="firstrow"))
    elif args.subcommand == "delete":
        try:
            is_success = api.delete_task(task_id=args.task_id)
            if is_success:
                print(f"Task {args.task_id} deleted")
        except Exception as error:
            print(error)
    elif args.subcommand == "done":
        try:
            is_success = api.close_task(task_id=args.task_id)
            if is_success:
                print(f"Task {args.task_id} marked as done")
        except Exception as error:
            print(error)
    elif args.subcommand == "view":
        try:
            task = api.get_task(task_id=args.task_id)
            print(json.dumps(task.to_dict(), indent=2))
        except Exception as error:
            print(error)