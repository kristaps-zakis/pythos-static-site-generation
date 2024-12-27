import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_eq(self):
        title = extract_title("# This is a title ")
        self.assertEqual(title, "This is a title")

    def test_missing_title(self):
        with self.assertRaises(Exception, msg='No title found'):
            extract_title("###This is not a title")

