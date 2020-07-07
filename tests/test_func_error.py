
'''Tests for so_lazy function errors'''

import unittest
from so_lazy import lazy, NoLoaderError

_DATA = []

@lazy()
def _default_func_no_args():
    return len(_DATA)

@lazy(loader='_custom_lazy_loader')
def _custom_func_no_args():
    return len(_DATA)

class FunctionErrorTests(unittest.TestCase):
    '''Test function lazy load errors'''

    def test_default_no_loader_error(self):
        '''Test for no loader error with defaults'''
        self.assertRaises(NoLoaderError, _default_func_no_args)

    def test_custom_no_loader_error(self):
        '''Test for no loader error with custom'''
        self.assertRaises(NoLoaderError, _custom_func_no_args)
