#! /usr/bin/env python
# -*- coding:utf-8; mode:python -*-

# Copyright (c) 2020 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import ilcli


class cmd1(ilcli.Command):

    serve_rest = True

    def _init_arguments(self):
        self.add_argument('arg1', help='the argument')

    def _verify_arguments(self, parsed_args):
        print('cmd1: verify args: ' + str(parsed_args))

    def _run(self, parsed_args):
        print('cmd1: running: ' + str(parsed_args))
        return 0


class cmd2(ilcli.Command):

    def _run(self, parsed_args):
        print('cmd2: running: ' + str(parsed_args))
        return 0

    def _verify_arguments(self, parsed_args):
        print('cmd2: verify args: ' + str(parsed_args))


class cmd3(ilcli.Command):
    subcommands = [cmd1, cmd2]

    def _init_arguments(self):
        self.add_argument('--common')


class mycmd(ilcli.Command):
    subcommands = [cmd1, cmd2, cmd3]


def test_mycmd():
    mycmd()
