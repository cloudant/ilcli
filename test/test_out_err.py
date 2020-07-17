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

import unittest

import ilcli

from .helpers import iostream


class PrintTests(unittest.TestCase):

    class out(ilcli.Command):
        def _init_arguments(self):
            self.add_argument('msg')

        def _run(self, args):
            self.out(args.msg)

    class err(ilcli.Command):
        def _init_arguments(self):
            self.add_argument('msg')

        def _run(self, args):
            self.err(args.msg)

    def setUp(self):
        self.out = iostream()
        self.err = iostream()
        self.out_cmd = PrintTests.out(out=self.out)
        self.err_cmd = PrintTests.err(err=self.err)

    def test_out_err_works(self):
        """
        Test basic behaviour of out() and err()
        """
        self.out_cmd.run(['msg to out'])
        self.err_cmd.run(['msg to err'])
        self.assertEqual('msg to out\n', self.out.getvalue())
        self.assertEqual('msg to err\n', self.err.getvalue())

    def test_out_with_args(self):
        """
        Test out() with arguments
        """
        self.out_cmd.out('hello %s', 'test!')
        self.assertEqual('hello test!\n', self.out.getvalue())

        self.out.seek(0)
        self.out_cmd.out('%s %s', 'hello', 'test!')
        self.assertEqual('hello test!\n', self.out.getvalue())

    def test_err_with_args(self):
        """
        Test err() with arguments
        """
        self.err_cmd.err('hello %s', 'test!')
        self.assertEqual('hello test!\n', self.err.getvalue())

        self.err.seek(0)
        self.err_cmd.err('%s %s', 'hello', 'test!')
        self.assertEqual('hello test!\n', self.err.getvalue())
