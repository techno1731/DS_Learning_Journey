#!/usr/bin/env python3
"""Test some base cases for for palindrome.py"""

import unittest
from findwords import findword


class TestFindWord(unittest.TestCase):
    """Class definition for test units of findword module """

    def test_base_findword(self):
        """Test the findword function base cases"""
        word1 = "donor"
        word2 = "donut"
        text= "Nabucodonosor"
        self.assertEqual(findword(word1,text), True)
        self.assertEqual(findword(word2,text), False)


if __name__ == "__main__":
    unittest.main()

