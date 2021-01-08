#!/usr/bin/env python3
"""Test some base cases for for palindrome.py"""

import unittest
from palindrome import prepare_text, palindrome


class TestPalindrome(unittest.TestCase):
    """Class definition for test units of palindrome """

    def test_base_prepare_text(self):
        """Test the text preparation base cases"""
        text_prepared = prepare_text("Ten animals I slam in a net")
        self.assertEqual(text_prepared, "tenanimalsislaminanet")

    def test_base_palindrome(self):
        """Test the palindrome function"""
        text_original1 = "Ten animals I slam in a net"
        text_original2 = "Eleven animals I slam in a net"
        text_prepared1 = prepare_text(text_original1)
        text_prepared2 = prepare_text(text_original2)
        self.assertEqual(palindrome(text_original1, text_prepared1),True)
        self.assertEqual(palindrome(text_original2, text_prepared2),False)


if __name__ == "__main__":
    unittest.main()
