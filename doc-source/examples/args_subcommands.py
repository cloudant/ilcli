#! /usr/bin/env python
# -*- coding:utf-8; mode:python -*-

import ilcli


class ssh(ilcli.Command):
    """
    ssh into a hostname
    """
    def _run(self, args):
        self.out('SSH into: %s', args.hostname)


class ping(ilcli.Command):
    """
    ping a hostname
    """
    def _run(self, args):
        self.out('Ping to: %s', args.hostname)


class net(ilcli.Command):
    """
    networking tools
    """
    subcommands = [ssh, ping]

    def _init_arguments(self):
        self.add_argument('hostname', help='target IP or hostname')


class ls(ilcli.Command):
    """
    list a file/directory
    """
    def _run(self, args):
        self.out('ls: %s', args.path)


class rm(ilcli.Command):
    """
    remove a file/directory
    """
    def _run(self, args):
        self.out('rm: %s', args.path)


class fs(ilcli.Command):
    """
    file-system tools
    """
    subcommands = [ls, rm]

    def _init_arguments(self):
        self.add_argument('path', help='path to file/dir')


class mytools(ilcli.Command):
    subcommands = [net, fs]

    def _init_arguments(self):
        self.add_argument(
            '-v', '--verbose', action='store_true', help='increase verbosity'
        )


exit(mytools().run())
