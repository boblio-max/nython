from .config import Config
from .sources import load_cli_args, load_env_vars

# Attach everything to the module namespace
import sys
this_module = sys.modules[__name__]

this_module.Config = Config
this_module.load_cli_args = load_cli_args
this_module.load_env_vars = load_env_vars
