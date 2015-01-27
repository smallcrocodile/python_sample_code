#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


def log(func):
    def wrapper(*args, **kw):
        print('Call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper

@log
def now():
    """

    :rtype : object
    """
    print(time.time())

now()