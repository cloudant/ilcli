#! /usr/bin/env python
# -*- coding:utf-8; mode:python -*-

import ilcli


class ls(ilcli.Command):
    """
    list a file/directory
    """
    man_page = 'ls'
    man_section = 1


exit(ls().run())
