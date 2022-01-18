"""task.py"""
import sys
import os
import argparse
from pathlib import Path
from tabulate import tabulate
from configparser import ConfigParser
from todoist_api_python.api import TodoistAPI

def run_task(args: argparse.ArgumentParser) -> None:
    home_dir = Path.home()
    config_file = os.path.join(home_dir, ".taoist/config.ini")
    config = ConfigParser()
    if os.path.isfile(config_file):
        config.read(config_file)
    else:
        print("Error: Cannot read API token, please run init function")
        sys.exit(1)
    api = TodoistAPI(config['Default']['token'])
    tasks = api.get_tasks()
    if args.subcommand == "list":
        task_list = [["id", "content", "status", "due"],]
        for task in tasks:
            status = "Open"
            if task.completed:
                status = "Done"
            row = [task.id, task.content, status, task.due.date]
            task_list.append(row)
        print(tabulate(task_list, headers="firstrow"))
