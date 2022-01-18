"""parse_args.py"""
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
        help="Todoist user account API token",
    )

    # Define parser for project function
    project_parser = subparsers.add_parser(
        "project", help="project-related functions"
    )

    # Add project subcommand parser
    project_subparser = project_parser.add_subparsers(dest="subcommand", help="subcommands")

    # Parse project/list
    project_list_subparser = project_subparser.add_parser("list", help="list projects")
 
    # Parse project/create
    project_create_subparser = project_subparser.add_parser("create", help="create project")
    project_create_subparser.add_argument(
        "project_name",
        action="store",
        metavar="NAME",
        type=str,
        help="name of new project to create",
    )

    # Parse project/delete
    project_delete_subparser = project_subparser.add_parser("delete", help="delete project")
    project_delete_subparser.add_argument(
        "project_id",
        action="store",
        metavar="PROJECT_ID",
        type=int,
        help="id of project to delete",
    )

    # Define parser for task function
    task_parser = subparsers.add_parser(
        "task", help="task-related functions"
    )

    # Add task subcommand parser
    task_subparser = task_parser.add_subparsers(dest="subcommand", help="subcommands")

    # Parse task/list
    task_list_subparser = task_subparser.add_parser("list", help="list tasks")
    task_list_subparser.add_argument(
        "--sort",
        action="store_true",
        help="sort tasks by due date",
    )

    # Parse task/view
    task_view_subparser = task_subparser.add_parser("view", help="view task details")
    task_view_subparser.add_argument(
        "task_id",
        action="store",
        metavar="TASK_ID",
        type=int,
        help="view task details",
    )

    # Parse task/create
    task_create_subparser = task_subparser.add_parser("create", help="create task")
    task_create_subparser.add_argument(
        "project_name",
        action="store",
        metavar="PROJECT_NAME",
        type=str,
        default="Inbox",
        help="create new task in given project [default: Inbox]",
    )

    # Parse task/delete
    task_delete_subparser = task_subparser.add_parser("delete", help="delete task")
    task_delete_subparser.add_argument(
        "task_id",
        action="store",
        metavar="TASK_ID",
        type=int,
        help="delete task",
    )

    # Parse task/edit
    task_edit_subparser = task_subparser.add_parser("edit", help="edit task")
    task_edit_subparser.add_argument(
        "task_id",
        action="store",
        metavar="TASK_ID",
        type=int,
        help="edit a specified task",
    )

    # Parse task/move
    task_move_subparser = task_subparser.add_parser("move", help="move task")
    task_move_subparser.add_argument(
        "task_id",
        action="store",
        metavar="TASK_ID",
        type=int,
        help="move task to new project",
    )
    task_move_subparser.add_argument(
        "--dest",
        action="store",
        metavar="PROJECT_ID",
        type=int,
        help="destination project id",
    )

    # Parse task/label
    task_label_subparser = task_subparser.add_parser("label", help="add label to task")
    task_label_subparser.add_argument(
        "task_id",
        action="store",
        metavar="TASK_ID",
        type=int,
        help="id of existing task to add label",
    )

    # Parse task/done
    task_done_subparser = task_subparser.add_parser("done", help="mark task as done")
    task_done_subparser.add_argument(
        "task_id",
        action="store",
        metavar="TASK_ID",
        type=int,
        help="id of task to mark as done",
    )

    # Parse arguments
    return parser.parse_args(args=None if sys.argv[1:] else ["--help"])