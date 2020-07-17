#! /usr/bin/env python
# -*- coding:utf-8; mode:python -*-

import ilcli


class mycmd(ilcli.Command):
    def _init_arguments(self):
        self.add_argument('message', help='your message')
        self.add_argument(
            '-u', '--upper', action='store_true', help='message in upper case'
        )

    def _run(self, args):
        msg = args.message
        if args.upper:
            msg = msg.upper()
        self.out(msg)
        return 0


cmd = mycmd()
cmd.run()  # sys.argv by default
cmd.run(['me too'])
cmd.run(['me too', '-u'])
cmd.run(['--upper', 'me too!!'])
