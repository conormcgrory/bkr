"""Module for handling application data stored in .bkr directory"""

import os

import toml

from . import errors


class Config:
    """Class for holding information from config file."""

    def __init__(self, fp):

        try:
            cfg_dict = toml.load(fp)
            self._code_path = cfg_dict['core']['code_path']
            self._results_path = cfg_dict['core']['results_path']

        except toml.decoder.TomlDecodeError:
            raise errors.InvalidConfigError('Not valid TOML')

        except KeyError as err:
            raise errors.InvalidConfigError(f'Missing required field: {err}')

    @property
    def code_path(self):
        return self._code_path

    @property
    def results_path(self):
        return self._results_path


class AppState:
    """Class for holding all application state."""

    def __init__(self, bkr_dir, config):

        self._bkr_dir = bkr_dir
        self._config = config

    @property
    def bkr_dir(self):
        return self._bkr_dir

    @property
    def config(self):
        return self._config


def get_bkr_dir():
    """Return path to .bkr directory for current working tree.

    Returns:
        path (str): Absoltue path to .bkr directory for current working tree,
            if it exists.
    Raises:
        ValueError: If there is no .bkr directory anywhere on the current 
            path.
    """

    def _get_bkr_dir(fpath):

        if os.path.isdir(f'{fpath}/.bkr'):
            return f'{fpath}/.bkr'
        elif fpath == '/':
            raise errors.NotInTreeError
        else:
            _get_bkr_dir(os.path.dirname(fpath))
    
    return _get_bkr_dir(os.getcwd())


def load_config(bkr_dir):
    """Get config information from bkr directory."""

    try:
        with open(f'{bkr_dir}/config.toml', 'r') as f:
            return Config(f)

    except FileNotFoundError:
        raise errors.ConfigNotFoundError


def get_state():
    """Get application state."""
    
    bkr_dir = get_bkr_dir()
    config = load_config(bkr_dir)

    return AppState(bkr_dir, config)
