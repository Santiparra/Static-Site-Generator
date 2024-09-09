class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    #A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    #An HTMLNode without a tag will just render as raw text
    self.tag = tag
    
    #A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    #An HTMLNode without a value will be assumed to have children
    self.value = value
    
    #A list of HTMLNode objects representing the children of this node
    #An HTMLNode without children will be assumed to have a value
    self.children = children
    
    """
    A dictionary of key-value pairs representing the attributes of the HTML tag. 
    For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    """
    # An HTMLNode without props simply won't have any attributes   
    self.props = props

  def to_html(self):
    raise NotImplementedError("to_html method not implemented")
    
  def props_to_html(self):
    html_props = ''
    if self.props is None:
      return ""    
    for prop in self.props:
      html_props += f' {prop}="{self.props[prop]}"'
    return html_props
    
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
