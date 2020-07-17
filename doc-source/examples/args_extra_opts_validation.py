#! /usr/bin/env python
# -*- coding:utf-8; mode:python -*-

import ilcli


class mycmd(ilcli.Command):

    extra_args = True

    def _init_arguments(self):
        self.add_argument('message', help='your message')

    def _validate_extra_arguments(self, args):
        self.kv = dict([args[0].split('=')])

    def _run(self, args):
        msg = args.message.format(**self.kv)
        self.out(msg)
        return 0


exit(mycmd().run())
