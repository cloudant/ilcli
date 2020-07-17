# -*- coding:utf-8; mode:python -*-


import io
import sys


def iostream(*args, **kwargs):
    if sys.version_info.major >= 3:
        return io.StringIO(*args, **kwargs)
    return io.BytesIO(*args, **kwargs)
