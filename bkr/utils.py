"""Utility functions for bkr code"""

import os

from . import git


def prompt_user_code_path():
    """Prompt user for path to Git repo containing code, and validate it."""

    while(True):

        input_path = input('Path to Git repo containing code:')
        abs_path = os.path.abspath(input_path)
        
        if git.is_valid_repo(abs_path):
            return abs_path
        else:
            print(f"'{abs_path}' is not a Git repo.")
            if raw_input('Continue? (y/n)') == 'n':
                raise ValueError('User failed to specify code path')


def prompt_user_results_path():
    """Prompt user for path to results directory, and validate it."""

    while(True):

        input_path = input('Path to results directory:')
        abs_path = os.path.abspath(input_path)
        
        if os.path.isdir(abs_path):
            return abs_path
        else:
            print(f"'{abs_path}' is not an existing directory.")
            if raw_input('Continue? (y/n)') == 'n':
                raise ValueError('User failed to specify code path')
