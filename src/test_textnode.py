import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_text_type(self):
        node1 = TextNode("Same text", TextType.BOLD, None)
        node2 = TextNode("Same text", TextType.ITALIC, None)
        self.assertNotEqual(node1, node2)

    def test_not_equal_url(self):
        node1 = TextNode("Image", TextType.IMAGE, "http://example.com/image.png")
        node2 = TextNode("Image", TextType.IMAGE, "http://different.com/image.png")
        self.assertNotEqual(node1, node2)

    def test_eq_with_url(self):
        node1 = TextNode("Link", TextType.LINK, "http://example.com")
        node2 = TextNode("Link", TextType.LINK, "http://example.com")
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
