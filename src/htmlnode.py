
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Child classes should override")
    
    def props_to_html(self):
        result = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return result
    
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"

# child classes

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError('value cannot be empty')
        if self.tag == None:
            return self.value
        else:
            props_string = ''
            if self.props:
                props_string = " " + self.props_to_html()
            result = f"<{self.tag}{props_string}>" + self.value + f"</{self.tag}>" 
            return result     