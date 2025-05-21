import unittest
from textnode import TextNode, TextType
from htmlnode import LeafNode
from convert_functions import text_node_to_html_node, split_nodes_image,split_nodes_link

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
    
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()