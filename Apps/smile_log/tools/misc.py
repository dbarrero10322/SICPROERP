# -*- coding: utf-8 -*-


import datetime
import traceback


def add_timing(original_method):
    def new_method(self, msg):
        delay = datetime.datetime.now() - self._logger_start
        msg += " after %sh %smin %ss" % tuple(str(delay).split(':'))
        return original_method(self, msg)
    return new_method


def add_trace(original_method):
    def new_method(self, msg):
        stack = traceback.format_exc()
        stack = stack.replace('%', '%%')
        msg += '\n%s' % stack
        return original_method(self, msg)
    return new_method
