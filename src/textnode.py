from constants import *

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
        return LeafNode(None, self.text)
      case text_type_bold:
      case text_type_italic:
      case text_type_code:
      case text_type_link:
      case text_type_image:
      case _:
        raise Exception("Invalid text type")