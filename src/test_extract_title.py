import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        self.assertEqual(extract_title("# Hello World"), "Hello World")
    
    def test_title_with_spaces(self):
        self.assertEqual(extract_title("#    Spacey   Title    "), "Spacey   Title")
    
    def test_no_title(self):
        with self.assertRaises(Exception):
            extract_title("Hello\nWorld")

    def test_multiple_headers(self):
        markdown = """# Main Title
        ## Second Title
        ### Third Title
        # Another Main Title"""
        self.assertEqual(extract_title(markdown), "Main Title")

    def test_title_with_empty_lines(self):
        markdown = "\n\n# Title After Empty Lines\n\n"
        self.assertEqual(extract_title(markdown), "Title After Empty Lines")

    def test_title_with_special_chars(self):
        self.assertEqual(extract_title("# Title with @#$%^&*"), "Title with @#$%^&*")

if __name__ == "__main__":
    unittest.main()