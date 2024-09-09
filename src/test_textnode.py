import unittest

from textnode import TextNode
from constants import *

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", text_type_text)
    node2 = TextNode("This is a text node", text_type_text)
    self.assertEqual(node, node2)

  def test_consts_work(self): 
    node = TextNode("This is a text node", text_type_bold, None)
    node2 = TextNode("This is a text node", "bold")
    self.assertEqual(node, node2)

  def test_eq2(self):
    node = TextNode("This is a text node", text_type_bold, "someurl/with.com")
    node2 = TextNode("This is a text node", text_type_bold, "someurl/with.com")
    self.assertEqual(node, node2)

  def test_diff(self):
    node = TextNode("This is text", text_type_bold)
    node2 = TextNode("This is a text node", text_type_bold)
    self.assertNotEqual(node, node2)

  def test_diff2(self):
    node = TextNode("This is a text node", text_type_bold)
    node2 = TextNode("This is a text node", text_type_italic)
    self.assertNotEqual(node, node2)  

  def test_diff3(self):
    node = TextNode("This is a text node", text_type_bold, "someurl/with.com")
    node2 = TextNode("This is a text node", text_type_bold)
    self.assertNotEqual(node, node2)

  def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )  

if __name__ == "__main__":
    unittest.main()