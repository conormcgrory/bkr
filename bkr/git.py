"""Module containing commands for Git"""

import os
import sh


def get_current_commit(code_path):
    """Return current commit of code in Git repo"""

    return sh.git('rev-parse', 'HEAD', _cwd=code_path).strip()


def is_valid_repo(fpath):
    """Return true if fpath points to a valid Git repo"""

    return os.path.isdir(fpath) and os.path.isdir(f'{fpath}/.git')
