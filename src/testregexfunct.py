import unittest
from textnode import TextNode, TextType
from convert_functions import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractors(unittest.TestCase):
    def test_extract_single_image(self):
        text = "Here is an image: ![Alt text](https://example.com/image.png)"
        expected = [("Alt text", "https://example.com/image.png")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)

    def test_extract_multiple_images(self):
        text = "One: ![A](url1.png) Two: ![B](url2.jpg)"
        expected = [("A", "url1.png"), ("B", "url2.jpg")]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)

    def test_extract_no_images(self):
        text = "Just some text and a [link](http://example.com)"
        expected = []
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)

    def test_extract_single_link(self):
        text = "Here is a [link](https://example.com)"
        expected = [("link", "https://example.com")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)

    def test_extract_multiple_links(self):
        text = "Links: [Google](https://google.com) and [GitHub](https://github.com)"
        expected = [("Google", "https://google.com"), ("GitHub", "https://github.com")]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)

    def test_extract_no_links(self):
        text = "Image only: ![img](https://img.com)"
        expected = []
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)

    def test_links_not_confused_with_images(self):
        text = "![img](https://img.com) and [link](https://link.com)"
        expected_img = [("img", "https://img.com")]
        expected_link = [("link", "https://link.com")]
        self.assertEqual(extract_markdown_images(text), expected_img)
        self.assertEqual(extract_markdown_links(text), expected_link)

if __name__ == "__main__":
    unittest.main()