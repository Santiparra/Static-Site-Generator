import unittest

from textnode import (
    TextNode,
    TextType,
)

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.TEXT)
    node2 = TextNode("This is a text node", TextType.TEXT)
    self.assertEqual(node, node2)

  def test_consts_work(self): 
    node = TextNode("This is a text node", TextType.BOLD, None)
    node2 = TextNode("This is a text node", "bold")
    self.assertEqual(node, node2)

  def test_eq2(self):
    node = TextNode("This is a text node", TextType.BOLD, "someurl/with.com")
    node2 = TextNode("This is a text node", TextType.BOLD, "someurl/with.com")
    self.assertEqual(node, node2)

  def test_diff(self):
    node = TextNode("This is text", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertNotEqual(node, node2)

  def test_diff2(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.ITALIC)
    self.assertNotEqual(node, node2)  

  def test_diff3(self):
    node = TextNode("This is a text node", TextType.BOLD, "someurl/with.com")
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertNotEqual(node, node2)

  def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )  

if __name__ == "__main__":
    unittest.main()
