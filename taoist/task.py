"""task.py"""
import sys
import os
import argparse
from pathlib import Path
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
        for task in tasks:
            print(task.id, "\t", task.content, "\t", task.completed, "\t", task.due.string)
