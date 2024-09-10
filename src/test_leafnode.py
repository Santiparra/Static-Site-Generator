import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

  def inheritance(self):
    leaf = LeafNode("p", "Hiya", {"class": "https://this.org"})
    self.assertEqual(isinstance(leaf, HTMLNode))
 
  def test_to_html_props(self):
    leaf = LeafNode(
      "div",
      "Hello, world!",
      {"class": "greeting", "href": "https://boot.dev"},
    )
    self.assertEqual(
      leaf.props_to_html(),
      ' class="greeting" href="https://boot.dev"',
    )

  def test_values(self):
    leaf = LeafNode(
      "h1",
      "too much coffee",
    )
    self.assertEqual(
      leaf.tag,
      "h1",
    )
    self.assertEqual(
      leaf.value,
      "too much coffee",
    )
    self.assertEqual(
      leaf.props,
      None,
    )

  def test_repr(self):
    leaf = LeafNode(
      "p",
      "What a strange world",
      {"class": "primary"}
    )
    self.assertEqual(
      leaf.__repr__(),
        "LeafNode(p, {'class': 'primary'}, What a strange world)",
      )

  def test_to_html_no_children(self):
    node = LeafNode("p", "Hello, world!")
    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

  def test_to_html_no_tag(self):
    node = LeafNode(None, "Hello, world!")
    self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()