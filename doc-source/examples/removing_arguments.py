#! /usr/bin/env python
# -*- coding:utf-8; mode:python -*-

from ilcli import Command


class FirstDemoCommand(Command):
    ignore_arguments = ['-b']

    def _init_arguments(self):
        super()._init_arguments()
        self.add_argument('--foo')


class SecondDemoCommand(FirstDemoCommand):
    ignore_arguments = ['--bar', '--foo']


class ThirdDemoCommand(FirstDemoCommand):
    ignore_arguments = ['bat']


class Parent(Command):

    subcommands = [FirstDemoCommand, SecondDemoCommand, ThirdDemoCommand]

    def _init_arguments(self):
        self.add_argument('-b', '--bar')
        self.add_argument('bat')


if __name__ == '__main__':
    exit(Parent().run())
