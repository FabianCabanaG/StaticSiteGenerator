import unittest
from htmlnode import HTMLNode  # asumiendo que tu clase está en htmlnode.py

class TestHTMLNode(unittest.TestCase):

    def test_constructor_full(self):
        node = HTMLNode(
            tag="a",
            value="Google",
            children=[],
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Google")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"href": "https://www.google.com", "target": "_blank"})

    def test_props_to_html(self):
        node = HTMLNode(
            tag="a",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        expected = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_repr_output(self):
        node = HTMLNode("p", "Hello", [], {"class": "text"})
        expected = 'HTMLNode(p,Hello,[],{\'class\': \'text\'})'
        self.assertEqual(repr(node), expected)

    def test_to_html_not_implemented(self):
        node = HTMLNode("p", "Hello")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_defaults_and_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

if __name__ == "__main__":
    unittest.main()