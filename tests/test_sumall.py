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

    def test_is_number(self):
        self.assertTrue(sumall.is_number('1'))

    def test_is_not_number(self):
        self.assertFalse(sumall.is_number('a'))

    def test_is_unicode_number(self):
        self.assertTrue(sumall.is_unicode_number('⅓'))

    def test_is_not_unicode_number(self):
        self.assertFalse(sumall.is_unicode_number('⅓a'))

    def test_get_line_total_number(self):
        line = '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "db367858-24f8-46ec-b352-08cdf5388ad4", "seqlen": 1177, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.995, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}'
        self.assertEqual(sumall.get_line_total(line), 1177)

    def test_get_line_total_number_fails(self):
        line = '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "db367858-24f8-46ec-b352-08cdf5388ad4", "seqlen": 1177, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.995, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}'
        self.assertNotEqual(sumall.get_line_total(line), 1176)

    def test_get_line_total_unicode_number(self):
        line = '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "db367858-24f8-46ec-b352-08cdf5388ad4", "seqlen": "⅓", "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.995, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}'
        self.assertEqual(sumall.get_line_total(line), 0.3333333333333333)

    def test_get_line_total_unicode_number_fails(self):
        line = '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "db367858-24f8-46ec-b352-08cdf5388ad4", "seqlen": 1177, "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.995, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}'
        self.assertNotEqual(sumall.get_line_total(line), 0.3333)

    def test_get_line_total_invalid_value(self):
        line = '{"format_conversion": {"alphabet_conversion": false, "header_corrected": false}, "barcode": "NA", "retcode": "PASS", "exit_status": "Workflow successful", "calibration": false, "barcode_detection": {"status": "1", "barcode": "NA", "barcode_score": 0.0}, "start_time": 1501853965, "read_id": "db367858-24f8-46ec-b352-08cdf5388ad4", "seqlen": "aaa", "filename": "split_aa.fastq", "runid": "f9b53105df0f6e165aa09f824bd26cbcb4dfa93a", "mean_qscore": 12.995, "software": {"time_stamp": "2019-Aug-22 09:38:14", "version": "3.10.0", "component": "homogeny"}}'
        self.assertRaises(Exception, sumall.get_line_total(line), line)

if __name__ == '__main__':
    unittest.main()