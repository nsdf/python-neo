#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests of neo.io.neomatlabio
"""

# needed for python 3 compatibility
from __future__ import absolute_import, division

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from neo.test.iotest.common_io_test import BaseTestIO
try:
    from neo.io import NeoMatlabIO
    can_run = True
except ImportError:
    can_run = False
    NeoMatlabIO = None


@unittest.skipUnless(can_run, "NeoMatlabIO not available")
class TestNeoMatlabIO(BaseTestIO, unittest.TestCase):
    ioclass = NeoMatlabIO
    files_to_test = []
    files_to_download = []


if __name__ == "__main__":
    unittest.main()
