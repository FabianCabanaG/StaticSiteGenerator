import unittest
from convert_functions import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):

    def test_basic_blocks(self):
        input_text = "# Heading\n\nParagraph\n\n- item 1\n- item 2"
        expected = [
            "# Heading",
            "Paragraph",
            "- item 1\n- item 2"
        ]
        self.assertEqual(markdown_to_blocks(input_text), expected)

    def test_blocks_with_spaces_and_tabs(self):
        input_text = "# Heading Paragraph"
        expected = [
            "# Heading Paragraph"
        ]
        self.assertEqual(markdown_to_blocks(input_text), expected)

    def test_blocks_with_extra_spaces(self):
        input_text = "  # Title  \n\n   Some text with spaces  \n\n - list item 1  \n- list item 2 "
        expected = [
            "# Title",
            "Some text with spaces",
            "- list item 1  \n- list item 2"
        ]
        self.assertEqual(markdown_to_blocks(input_text), expected)

    def test_single_block_no_double_newline(self):
        input_text = "This is a single block of text without double newline"
        expected = [
            "This is a single block of text without double newline"
        ]
        self.assertEqual(markdown_to_blocks(input_text), expected)

    def test_multiple_consecutive_double_newlines(self):
        input_text = "First block\n\n\n\nSecond block\n\n\nThird block"
        expected = [
            "First block",
            "Second block",
            "Third block"
        ]
        self.assertEqual(markdown_to_blocks(input_text), expected)

if __name__ == "__main__":
    unittest.main()