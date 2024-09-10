from leafnode import LeafNode
from markdown_link_extractor import (
    extract_markdown_links,
    extract_markdown_images,
)

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

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
  if text_node.text_type == text_type_text:
    return LeafNode(None, text_node.text)
  if text_node.text_type == text_type_bold:
    return LeafNode("b", text_node.text)
  if text_node.text_type == text_type_italic:
    return LeafNode("i", text_node.text)
  if text_node.text_type == text_type_code:
    return LeafNode("code", text_node.text)
  if text_node.text_type == text_type_link:
    return LeafNode("a", text_node.text, {"href": text_node.url})
  if text_node.text_type == text_type_image:
    return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
  raise ValueError(f"Invalid text type: {text_node.text_type}")


def split_nodes_image(old_nodes):
  new_nodes = []
  for node in old_nodes:
    if node.text_type is not text_type_text:
      new_nodes.append(node)
      continue
    nodes_text = node.text  
    images = extract_markdown_images(nodes_text)    
    if len(images) is 0 :
      new_nodes.append(node)
      continue
    for image in images:
      splitted = nodes_text.split(f"![{image[0]}]({image[1]})", 1)
      if len(splitted) is not 2:
        raise Exception("Text provided contains invalid markdown syntax, markdown must contain open and closing delimiters")
      if splitted[0] is not "":
        new_nodes.append(TextNode(splitted[0], text_type_text))
      else:  
        new_nodes.append(TextNode(image[0], text_type_image, image[1]))
        nodes_text = splitted[1]
    if nodes_text is not "":
      new_nodes.append(TextNode(nodes_text, text_type_text)) 
  return new_nodes

def split_nodes_link(old_nodes):
  new_nodes = []
  for node in old_nodes:
    if node.text_type is not text_type_text:
      new_nodes.append(node)
      continue
    nodes_text = node.text  
    links = extract_markdown_links(nodes_text)    
    if len(links) is 0 :
      new_nodes.append(node)
      continue
    for link in links:
      splitted = nodes_text.split(f"[{link[0]}]({link[1]})", 1)
      if len(splitted) is not 2:
        raise Exception("Text provided contains invalid markdown syntax, markdown must contain open and closing delimiters")
      if splitted[0] is not "":
        new_nodes.append(TextNode(splitted[0], text_type_text))
      else:  
        new_nodes.append(TextNode(link[0], text_type_link, link[1]))
        nodes_text = splitted[1]
    if nodes_text is not "":
      new_nodes.append(TextNode(nodes_text, text_type_text)) 
  return new_nodes  