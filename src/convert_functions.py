from textnode import TextType, TextNode
from htmlnode import LeafNode
import re

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode('b',text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode('i',text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode('code',text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode('a',text_node.text,{"href":text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode('img','',{'src':text_node.url,'alt':text_node.text})
    else:
        raise Exception('Using an invalid TextType instance')

def split_nodes_delimiter(old_nodes, delilmiter, text_type=TextType):
    new_nodes = []
    for el in old_nodes:
        split = el.text.split(delilmiter)
        for i,e in enumerate(split):
            if e:
                if (i+1) % 2 == 0:
                    new_nodes.append(TextNode(e,text_type))
                else:
                    new_nodes.append(TextNode(e,TextType.TEXT))
                i += 1
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    input_nodes =  [TextNode(text,TextType.TEXT)]
    output_nodes = split_nodes_image(input_nodes)
    output_nodes = split_nodes_link(output_nodes)
    output_nodes = split_nodes_delimiter(output_nodes, "**", TextType.BOLD)
    output_nodes = split_nodes_delimiter(output_nodes, "_", TextType.ITALIC)
    output_nodes = split_nodes_delimiter(output_nodes, "`", TextType.CODE)

    return output_nodes
    
    

        