"""Main script for bkr application"""

import sys
import os
import argparse

import toml


# TODO: Add Git repo validation to this function
def _get_code_path():

    while(true):

        input_path = raw_input('Path to Git repo containing code:')
        abs_path = os.path.abspath(input_path)
        
        if os.path.isdir(abs_path):
            return abs_path
        else:
            print(f"'{abs_path}' is not a valid Git repo.")
            if raw_input('Continue? (y/n)') == 'n':
                raise ValueError('User failed to specify code path')


def _get_results_path():

    while(true):

        input_path = raw_input('Path to results directory:')
        abs_path = os.path.abspath(input_path)
        
        if os.path.isdir(abs_path):
            return abs_path
        else:
            print(f"'{abs_path}' is not a valid directory name.")
            if raw_input('Continue? (y/n)') == 'n':
                raise ValueError('User failed to specify code path')


def _write_config_file(code_path, results_path):

    config_dict = {
        'core': {
            'code_path': code_path,
            'results_path': results_path,
        }
    }

    with open('.bkr/config.toml', 'w') as f:
        toml.dump(config_dict, f)


def cmd_init(args):

    try:
        os.mkdir('.bkr')
        code_path = _get_code_path()
        results_path = _get_results_path()
        _write_config_file(code_path, results_path)

    except FileExistsError:
        print("Error: Directory '.bkr' already exists.")

    except (ValueError, IOError):
        print('Error: Unable to initialize bkr')

    else:
        print('Successfully initialized bkr')


def parse_args():
    
    parser = argparse.ArgumentParser(
        description='Command-line utility for experiment bookkeeping'
    )
    subparsers = parser.add_subparsers()

    parser_init = subparsers.add_parser(
        'init', 
        description='Initialize bkr in current directory'
    )
    parser_init.set_defaults(func=cmd_init)

    return parser.parse_args()


def main():

    args = parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
