#!/usr/bin/env python3

# Unit tests for the sumall script

# Author: Dean Layton-James
# Date Created: 2021-12-22
# Last Update: 2021-12-22
# Code Style: PEP 8

# Import required packages
import glob
import locale
import json
import os
import sys
import unicodedata
import unittest
from pathlib import Path

import sumall
from sumall import *

class TestSumall(unittest.TestCase):
    def test_check_path_local_path(self):
        self.assertEqual(sumall.check_data_path('./test_path'), 'test_path/')

    def test_check_path_fully_qualified_path(self):
        self.assertEqual(sumall.check_data_path('/tmp'), '/tmp/')

    def test_check_path_relative_path(self):
        self.assertEqual(sumall.check_data_path('../data'), '../data/')

    def test_check_path_folder_does_not_exist(self):
        self.assertRaises(Exception, sumall.check_data_path, '/tmp10')



if __name__ == '__main__':
    unittest.main()