"""task.py"""
import argparse
from taoist.read_config import read_config
from tabulate import tabulate
from todoist_api_python.api import TodoistAPI

def run_task(args: argparse.ArgumentParser) -> None:
    """
    Run the task command
    """

    # Read taoist user configuration
    config = read_config()

    # Initialize Todoist API
    api = TodoistAPI(config['Default']['token'])

    # Get tasks
    tasks = api.get_tasks()

    # Process subcommand
    if args.subcommand == "list":
        task_list = [["id", "content", "status", "due"],]
        for task in tasks:
            status = "Open"
            if task.completed:
                status = "Done"
            row = [task.id, task.content, status, task.due.date]
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