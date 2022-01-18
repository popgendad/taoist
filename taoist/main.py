"""main.py"""
from taoist.parse import parse_args
from taoist.task import run_task
from taoist.project import run_project
from taoist.init import run_init

def main():
    """
    Entry point for taoist program
    """

    # Parse arguments
    args = parse_args()

    # Fork execution stream
    if args.command == "project":
        run_project(args)
    elif args.command == "task":
        run_task(args)
    elif args.command == "init":
        run_init(args)
    else:
        raise Exception(f"Command {args.command} not recognized")

if __name__ == "__main__":
    main()
