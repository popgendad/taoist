"""init.py"""
import os
from pathlib import Path
from configparser import ConfigParser

def run_init(args):
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
    config['Default'] = {'token': args.token}
    with open(config_file, 'w') as config_stream:
        config.write(config_stream)
