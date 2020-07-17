#! /usr/bin/env python
# -*- coding:utf-8; mode:python -*-

import ilcli


class ls(ilcli.Command):
    """
    list a file/directory
    """
    inherit_arguments = False

    def _init_arguments(self):
        self.add_argument(
            '-v', '--version', action='store_true', help='show version'
        )

    def _validate_arguments(self, args):
        print('validate arguments at "ls"')

    def _run(self, args):
        print('Running ls')


class rm(ilcli.Command):
    """
    rm a file/directory
    """

    def _validate_arguments(self, args):
        print('validate arguments at "rm"')

    def _run(self, args):
        print('Running rm')


class fs(ilcli.Command):
    subcommands = [ls, rm]

    def _init_arguments(self):
        self.add_argument(
            '-v', '--verbose', action='store_true', help='increase verbosity'
        )

    def _validate_arguments(self, args):
        print('validate arguments at "fs"')


exit(fs().run())
