from ast import parse
import argparse, os
import re

def load_cli_args(keys):
    parser = argparse.ArgumentParser(description="Load configuration from CLI path.")
    for key in keys:
        parser.add_argument(f'--{key}', type=str, help=f'Path for {key}')
    args, _ = parser.parse_known_args()
    cli_paths = {key: getattr(args, key) for key in keys if getattr(args, key) is not None}
    return cli_paths

def load_env_vars(keys):
    data = {}
    for key in keys:
        env_value = os.getenv(key.upper())
        if env_value is not None:
            data[key] = env_value
    return data
