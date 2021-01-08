#!/usr/bin/env python3

import unittest
from C2FP import extract_regex_syslog, create_dictionary, create_csv_files


class TestLogAnalysis(unittest.TestCase):
    def test_extract_regex_syslog_base(self):
        line_error, line_info = extract_regex_syslog("syslog.log")
        self.assertEqual(line_error[0][1].strip(), "ERROR")
        self.assertEqual(line_error[0][3].strip(), "ennio.maldonado")
        self.assertEqual(line_error[0][2].strip(), "galleta not found")
        self.assertEqual(line_info[0][1], "INFO")
        self.assertEqual(line_info[0][2], "ennio.maldonado")

    def test_create_dictionary_base(self):
        line_error, line_info = extract_regex_syslog("syslog.log")
        dict_error, dict_stat= create_dictionary(line_error, line_info)
        self.assertEqual(dict_error['Error'],['Connection to DB failed','galleta not found'])
        self.assertEqual(dict_error['Count'],[2,1])
        self.assertEqual(dict_stat['Username'],['ennio.maldonado','julio','koncha','mike'])


if __name__ == "__main__":
    unittest.main()
