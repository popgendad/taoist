"""init.py"""
import os
import argparse
from pathlib import Path
from configparser import ConfigParser

def run_init(args: argparse.ArgumentParser) -> None:
    """
    Initialize Todoist account with API token
    """

    home_dir = Path.home()
    taoist_dir = os.path.join(home_dir, ".taoist")
    config_file = os.path.join(taoist_dir, "config.ini")
    config = ConfigParser()
    if os.path.isdir(taoist_dir):
        if os.path.isfile(config_file):
            config.read(config_file)
    else:
        os.mkdir(taoist_dir)
    if not args.token:
        token = input('Enter Your Todoist API Token: ')
        config['Default'] = {'token': token}
    else:
        config['Default'] = {'token': args.token}
    with open(config_file, 'w') as config_stream:
        config.write(config_stream)
    os.chmod(config_file, 0o600)
