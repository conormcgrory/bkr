"""CLI script for bkr application"""

import sys
import argparse

from . import commands
from . import errors


def parse_args():
    """Parse program arguments."""
    
    parser = argparse.ArgumentParser(
        description='Command-line utility for experiment bookkeeping'
    )
    subparsers = parser.add_subparsers()

    # Parser for 'init' command
    ps_init = subparsers.add_parser(
        'init', 
        description='Initialize bkr in current directory'
    )
    ps_init.set_defaults(cmd='init')

    # Parser for 'new' command
    ps_new = subparsers.add_parser('new', description='Create new record')
    ps_new.add_argument(
        '--name', 
        '-n', 
        default=None, 
        help='Name for experiment'
    )
    ps_new.set_defaults(cmd='new')

    # Pass '--help' if no arguments are passed
    s_args = sys.argv[1:] if len(sys.argv[1:]) > 0 else ['--help']

    return parser.parse_args(s_args)


def main():
    """Application main method."""

    args = parse_args()

    if args.cmd == 'init':
        commands.init(args)
    elif args.cmd == 'new':
        commands.new(args)
    else:
        raise NotImplementedError


if __name__ == '__main__':
    main()
