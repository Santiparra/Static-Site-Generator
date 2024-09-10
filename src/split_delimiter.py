from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for node in old_nodes:
    if node.text_type is not text_type_text:
      new_nodes.append(node)
      continue
    splitted = []
    children = node.text.split(delimiter)  
    if children.count(delimiter) % 2 != 0:
      raise Exception("Text contains invalid markdown syntax, markdown must contain open and closing delimiters")
    for i in range(len(children)):
      if children[i] == "":
        continue
      if i % 2 == 0:
        splitted.append(TextNode(children[i], text_type_text))
      else:  
        splitted.append(TextNode(children[i], text_type))    
    new_nodes.extend(splitted)
  return new_nodes  