import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )

    def test_missing_tag_raises_error(self):
        child = LeafNode("p", "text")
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [child]).to_html()
        self.assertEqual(str(context.exception), "tag attribute is not defined")

    def test_missing_children_raises_error(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", None).to_html()
        self.assertEqual(str(context.exception), "children attribute is not defined")

    def test_multiple_children(self):
        c1 = LeafNode("p", "first")
        c2 = LeafNode("p", "second")
        node = ParentNode("div", [c1, c2])
        self.assertEqual(node.to_html(), "<div><p>first</p><p>second</p></div>")

    def test_nested_with_props(self):
        child = LeafNode("a", "link", {"href": "https://example.com"})
        parent = ParentNode("p", [child], {"class": "highlight"})
        self.assertEqual(
            parent.to_html(),
            '<p><a href="https://example.com">link</a></p>'
        )

    def test_deeply_nested_structure(self):
        deepest = LeafNode("code", "print('Hello')")
        middle = ParentNode("pre", [deepest])
        top = ParentNode("div", [middle])
        self.assertEqual(top.to_html(), "<div><pre><code>print('Hello')</code></pre></div>")

if __name__ == "__main__":
    unittest.main()