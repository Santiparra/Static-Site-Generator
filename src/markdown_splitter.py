import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != text_type_text:
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

def split_nodes_image(old_nodes):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != text_type_text:
      new_nodes.append(node)
      continue
    nodes_text = node.text  
    images = extract_markdown_images(nodes_text)    
    if len(images) == 0 :
      new_nodes.append(node)
      continue
    for image in images:
      splitted = nodes_text.split(f"![{image[0]}]({image[1]})", 1)
      if len(splitted) != 2:
        raise ValueError("Text provided contains invalid markdown syntax, markdown must contain open and closing delimiters")
      if splitted[0] != "":
        new_nodes.append(TextNode(splitted[0], text_type_text))  
      new_nodes.append(TextNode(image[0], text_type_image, image[1]))
      nodes_text = splitted[1]
    if nodes_text != "":
      new_nodes.append(TextNode(nodes_text, text_type_text)) 
  return new_nodes

def split_nodes_link(old_nodes):
  new_nodes = []
  for node in old_nodes:
    if node.text_type != text_type_text:
      new_nodes.append(node)
      continue
    nodes_text = node.text  
    links = extract_markdown_links(nodes_text)    
    if len(links) == 0 :
      new_nodes.append(node)
      continue
    for link in links:
      splitted = nodes_text.split(f"[{link[0]}]({link[1]})", 1)
      if len(splitted) != 2:
        raise ValueError("Text provided contains invalid markdown syntax, markdown must contain open and closing delimiters")
      if splitted[0] != "":
        new_nodes.append(TextNode(splitted[0], text_type_text)) 
      new_nodes.append(TextNode(link[0], text_type_link, link[1]))
      nodes_text = splitted[1]
    if nodes_text != "":
      new_nodes.append(TextNode(nodes_text, text_type_text)) 
  return new_nodes  

def extract_markdown_images(text):
  matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
  return matches

def extract_markdown_links(text):  
  matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
  return matches