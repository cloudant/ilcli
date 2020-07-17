#! /usr/bin/env python
# -*- coding:utf-8; mode:python -*-

import ilcli


class mycmd(ilcli.Command):
    def _init_arguments(self):
        self.add_argument('message', help='your message')
        self.add_argument(
            '-u', '--upper', action='store_true', help='message in upper case'
        )

    def _validate_arguments(self, args):
        msg = args.message.lower()
        if 'ilcli' in msg:
            self.err("Please do not take ilcli's name in vain")
            return 1
        if 'help' in msg:
            self.out('You say help? Sure!')
            self.parser.print_help()
            return 0

    def _run(self, args):
        msg = args.message
        if args.upper:
            msg = msg.upper()
        self.out(msg)
        return 0


exit(mycmd().run())
