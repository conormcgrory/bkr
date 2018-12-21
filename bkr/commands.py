"""Commands for bkr application."""

import os
from datetime import datetime as dt

import toml

from . import errors
from . import utils
from . import app_data
from . import git


def init(args):
    """Process 'init' command."""

    try:
        os.mkdir('.bkr')
        config_dict = {
            'core': {
                'code_path': utils.prompt_user_code_path(),
                'results_path': utils.prompt_user_results_path(),
            }
        }
        with open('.bkr/config.toml', 'w') as f:
            toml.dump(config_dict, f)

    except FileExistsError:
        raise errors.InitError("Directory '.bkr' already exists.")

    except (ValueError, IOError):
        raise errors.InitError('Unable to initialize bkr')

    else:
        print('Successfully initialized bkr')


def new(args):
    """Process 'new' command."""

    rec_name = args.name
    if args.name is None:
        now_str = dt.now().strftime('%Y%m%dT%H%M')
        rec_name = f'rec_{now_str}'

    app_state = app_data.get_state()
    results_path = app_state.config.results_path
    code_path = app_state.config.code_path
    rec_path = f'{results_path}/{rec_name}'
    
    try:
        os.mkdir(rec_path)
        info_dict = {
            'name': rec_name,
            'code': {
                'commit': git.get_current_commit(code_path)
            }
        }

        with open(f'{rec_path}/info.toml', 'w') as f:
            toml.dump(info_dict, f)
        
    except FileExistsError:
        raise errors.RecordExistsError

    else:
        print(f"Successfully created record '{rec_name}'")
