#! /usr/bin/env python
# -*- coding:utf-8; mode:python -*-

import ilcli


class mycmd(ilcli.Command):
    def _run(self, args):
        self.out('Hello World!')
        return 0


exit(mycmd().run())
