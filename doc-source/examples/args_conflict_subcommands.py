#! /usr/bin/env python
# -*- coding:utf-8; mode:python -*-

import ilcli


class subcommand1(ilcli.Command):
    """
    --foo does different things
    """

    def _init_arguments(self):
        self.add_argument('-o', '--foo', help='new foo help')

    def _run(self, args):
        self.out('called with: {}'.format(args))


class subcommand2(ilcli.Command):
    """
    --foo does different things
    """

    def _init_arguments(self):
        self.add_argument('-f', '--far', help='new far help')

    def _run(self, args):
        self.out('called with: {}'.format(args))


class subcommand3(ilcli.Command):
    """
    This command replaces the parent definition of -f/--foo entirely
    """

    def _init_arguments(self):
        self.add_argument('-f', '--foo', help='new foo help')

    def _run(self, args):
        self.out('called with: {}'.format(args))


class toplevel(ilcli.Command):
    subcommands = [subcommand1, subcommand2, subcommand3]
    parser_args = {'conflict_handler': 'resolve'}

    def _init_arguments(self):
        self.add_argument(
            '-f', '--foo', help='old foo help'
        )
        self.add_argument(
            '-b', '--bar', help='old bar help'
        )


exit(toplevel().run())
