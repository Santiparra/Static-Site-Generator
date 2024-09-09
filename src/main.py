from textnode import TextNode
from constants import *

def main():
  dummy_node = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
  return print(dummy_node.__repr__())

main()  