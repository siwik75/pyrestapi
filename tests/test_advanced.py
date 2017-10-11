# -*- coding: utf-8 -*-

from .context import pyrestapi

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        pyrestapi.hmm()


if __name__ == '__main__':
    unittest.main()
