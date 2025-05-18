import unittest
from textnode import TextNode, TextType
from htmlnode import LeafNode
from convert_functions import text_node_to_html_node 

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node(self):
        node = TextNode("Hello", TextType.TEXT)
        expected = LeafNode(value="Hello")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_bold_node(self):
        node = TextNode("Bold", TextType.BOLD)
        expected = LeafNode("b", "Bold")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_italic_node(self):
        node = TextNode("Italic", TextType.ITALIC)
        expected = LeafNode("i", "Italic")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_code_node(self):
        node = TextNode("print('hello')", TextType.CODE)
        expected = LeafNode("code", "print('hello')")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_link_node(self):
        node = TextNode("Google", TextType.LINK, "https://www.google.com")
        expected = LeafNode("a", "Google", {"href": "https://www.google.com"})
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_image_node(self):
        node = TextNode("Logo", TextType.IMAGE, "https://img.com/logo.png")
        expected = LeafNode("img", "", {"src": "https://img.com/logo.png", "alt": "Logo"})
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_invalid_type_raises(self):
        with self.assertRaises(Exception):
            TextNode("Invalid", "UNKNOWN")
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()