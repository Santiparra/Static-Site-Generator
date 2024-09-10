from htmlnode import HTMLNode 

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):   
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("All parent nodes must have a tag")
    if self.children is None:
      raise ValueError("Children values must be provided for parent nodes") 
    children_converted = ""
    for item in self.children:
      children_converted += item.to_html()
    return f"<{self.tag}{self.props_to_html()}>{children_converted}</{self.tag}>"  

  def __repr__(self):
    return f"ParentNode({self.tag}, {self.children}, {self.props})"    