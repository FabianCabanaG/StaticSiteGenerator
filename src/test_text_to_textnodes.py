import unittest
from textnode import TextNode, TextType
from convert_functions import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):

    def test_plain_text(self):
        result = text_to_textnodes("Just plain text.")
        expected = [TextNode("Just plain text.", TextType.TEXT, None)]
        self.assertEqual(result, expected)

    def test_bold_text(self):
        result = text_to_textnodes("This is **bold** text.")
        expected = [
            TextNode("This is ", TextType.TEXT, None),
            TextNode("bold", TextType.BOLD, None),
            TextNode(" text.", TextType.TEXT, None),
        ]
        self.assertEqual(result, expected)

    def test_italic_text(self):
        result = text_to_textnodes("This is _italic_ text.")
        expected = [
            TextNode("This is ", TextType.TEXT, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(" text.", TextType.TEXT, None),
        ]
        self.assertEqual(result, expected)

    def test_code_text(self):
        result = text_to_textnodes("Use `code` here.")
        expected = [
            TextNode("Use ", TextType.TEXT, None),
            TextNode("code", TextType.CODE, None),
            TextNode(" here.", TextType.TEXT, None),
        ]
        self.assertEqual(result, expected)

    def test_image_markdown(self):
        result = text_to_textnodes("Look at this ![alt](img.png)")
        expected = [
            TextNode("Look at this ", TextType.TEXT, None),
            TextNode("alt", TextType.IMAGE, "img.png"),
        ]
        self.assertEqual(result, expected)

    def test_link_markdown(self):
        result = text_to_textnodes("Go to [Google](https://google.com)")
        expected = [
            TextNode("Go to ", TextType.TEXT, None),
            TextNode("Google", TextType.LINK, "https://google.com"),
        ]
        self.assertEqual(result, expected)

    def test_link_and_image(self):
        result = text_to_textnodes("Click [here](http://link.com) or see ![pic](img.jpg)")
        expected = [
            TextNode("Click ", TextType.TEXT, None),
            TextNode("here", TextType.LINK, "http://link.com"),
            TextNode(" or see ", TextType.TEXT, None),
            TextNode("pic", TextType.IMAGE, "img.jpg"),
        ]
        self.assertEqual(result, expected)

    def test_mixed_styles(self):
        result = text_to_textnodes("This is **bold**, _italic_, and `code`.")
        expected = [
            TextNode("This is ", TextType.TEXT, None),
            TextNode("bold", TextType.BOLD, None),
            TextNode(", ", TextType.TEXT, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(", and ", TextType.TEXT, None),
            TextNode("code", TextType.CODE, None),
            TextNode(".", TextType.TEXT, None),
        ]
        self.assertEqual(result, expected)

    def test_all_in_one(self):
        result = text_to_textnodes("This is **bold** and _italic_, with a [link](http://test.com) and an ![image](img.png).")
        expected = [
            TextNode("This is ", TextType.TEXT, None),
            TextNode("bold", TextType.BOLD, None),
            TextNode(" and ", TextType.TEXT, None),
            TextNode("italic", TextType.ITALIC, None),
            TextNode(", with a ", TextType.TEXT, None),
            TextNode("link", TextType.LINK, "http://test.com"),
            TextNode(" and an ", TextType.TEXT, None),
            TextNode("image", TextType.IMAGE, "img.png"),
            TextNode(".", TextType.TEXT, None),
        ]
        self.assertEqual(result, expected)

    def test_multiple_same_type(self):
        result = text_to_textnodes("**bold1** and **bold2**")
        expected = [
            TextNode("bold1", TextType.BOLD, None),
            TextNode(" and ", TextType.TEXT, None),
            TextNode("bold2", TextType.BOLD, None),
        ]
        self.assertEqual(result, expected)

    def test_edge_case_empty_text(self):
        result = text_to_textnodes("")
        expected = []
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
