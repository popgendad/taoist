"""parse.py"""
import sys
import argparse
from taoist import __version__

def parse_args() -> argparse.ArgumentParser:
    """
    Parse arguments for taoist program
    """

    parser = argparse.ArgumentParser(
        prog="taoist", description="Command line interface for Todoist"
    )
    parser.add_argument("--version", action="version", version=__version__)
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Define parser for init function
    init_parser = subparsers.add_parser("init", help="authenticate to Todoist API")
    init_parser.add_argument(
        "--token",
        action="store",
        metavar="TOKEN",
        type=str,
        help="Todoist API token",
    )

    # Define parser for project function
    project_parser = subparsers.add_parser(
        "project", help="project-related functions"
    )

    project_subparser = project_parser.add_subparsers(dest="subcommand", help="subcommands")

    project_list_subparser = project_subparser.add_parser("list", help="list projects")
    project_list_subparser.add_argument(
        "id",
        action="store",
        metavar="INPUT_FILE",
        type=str,
        help="file with merged bcsys output JSON files",
    )
    project_create_subparser = project_subparser.add_parser("create", help="create project")
    project_create_subparser.add_argument(
        "input",
        action="store",
        metavar="INPUT_FILE",
        type=str,
        help="file with merged bcsys output JSON files",
    )
    project_delete_subparser = project_subparser.add_parser("delete", help="delete project")
    project_delete_subparser.add_argument(
        "input",
        action="store",
        metavar="INPUT_FILE",
        type=str,
        help="file with merged bcsys output JSON files",
    )

    # Define parser for task function
    task_parser = subparsers.add_parser(
        "task", help="task-related functions"
    )
    task_subparser = task_parser.add_subparsers(dest="subcommand", help="subcommands")
    task_list_subparser = task_subparser.add_parser("list", help="list tasks")
    task_list_subparser.add_argument(
        "input",
        action="store",
        metavar="INPUT_FILE",
        type=str,
        help="file with merged bcsys output JSON files",
    )
    task_create_subparser = task_subparser.add_parser("create", help="create task")
    task_create_subparser.add_argument(
        "input",
        action="store",
        metavar="INPUT_FILE",
        type=str,
        help="file with merged bcsys output JSON files",
    )
    task_delete_subparser = task_subparser.add_parser("delete", help="delete task")
    task_delete_subparser.add_argument(
        "input",
        action="store",
        metavar="INPUT_FILE",
        type=str,
        help="file with merged bcsys output JSON files",
    )
    task_edit_subparser = task_subparser.add_parser("edit", help="edit task")
    task_edit_subparser.add_argument(
        "input",
        action="store",
        metavar="INPUT_FILE",
        type=str,
        help="file with merged bcsys output JSON files",
    )
    task_move_subparser = task_subparser.add_parser("move", help="move task")
    task_move_subparser.add_argument(
        "input",
        action="store",
        metavar="INPUT_FILE",
        type=str,
        help="file with merged bcsys output JSON files",
    )
    task_tag_subparser = task_subparser.add_parser("tag", help="add tag to task")
    task_tag_subparser.add_argument(
        "input",
        action="store",
        metavar="INPUT_FILE",
        type=str,
        help="file with merged bcsys output JSON files",
    )
    task_done_subparser = task_subparser.add_parser("delete", help="mark task as done")
    task_done_subparser.add_argument(
        "input",
        action="store",
        metavar="INPUT_FILE",
        type=str,
        help="file with merged bcsys output JSON files",
    )

    # Parse arguments
    return parser.parse_args(args=None if sys.argv[1:] else ["--help"])