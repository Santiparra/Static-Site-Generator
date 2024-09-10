from constants import *
from leafnode import LeafNode

class TextNode:
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other_node):
    if isinstance(other_node, TextNode):
      return (
        self.text == other_node.text and 
        self.text_type == other_node.text_type and 
        self.url == other_node.url
      )
    return False

  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type}, {self.url})"

  def text_node_to_html_node(text_node):
    match text_node.text_type:
      case text_type_text:
        return LeafNode(None, text_node.text)
      case text_type_bold:
        return LeafNode("b", text_node.text)
      case text_type_italic:
        return LeafNode("i", text_node.text)
      case text_type_code:
        return LeafNode("code", text_node.text)
      case text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
      case text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
      case _:
        raise Exception("Invalid text type")