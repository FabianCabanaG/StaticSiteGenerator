import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leafnode_with_tag_and_props(self):
        node = LeafNode("a", "Google", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Google</a>'
        self.assertEqual(node.to_html(), expected)

    def test_leafnode_without_props(self):
        node = LeafNode("p", "Hello world", None)
        expected = "<p>Hello world</p>"
        self.assertEqual(node.to_html(), expected)

    def test_leafnode_tag_none(self):
        node = LeafNode(None, "Just text", None)
        expected = "Just text"
        self.assertEqual(node.to_html(), expected)

    def test_leafnode_multiple_props(self):
        node = LeafNode("img", "Image", {"src": "image.jpg", "alt": "My image"})
        expected = '<img src="image.jpg" alt="My image">Image</img>'
        self.assertEqual(node.to_html(), expected)

    def test_leafnode_raises_value_error_on_none_value(self):
        node = LeafNode("span", None, None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()