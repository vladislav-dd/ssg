from markdown_blocks import markdown_to_html_node
from htmlnode import ParentNode
from extract_title import extract_title
import os
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path,"r") as f:
        text = f.read()
        f.close()
    
    with open(template_path, "r") as t:
        template_file = t.read()
        t.close()

    html_nodes = markdown_to_html_node(text)
    content = ParentNode.to_html(html_nodes)
    title = extract_title(text)
    
    final_html = template_file.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", content)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    Path(dest_dir_path).mkdir(exist_ok=True, parents=True)
    list_dir = os.listdir(dir_path_content)
    for entry in list_dir:
        entry_path = os.path.join(dir_path_content, entry)
        relative_path = entry_path[len(dir_path_content):]
        if relative_path.startswith('/'):
            relative_path = relative_path[1:]
        if entry_path.endswith(".md"):
            new_dest_path = os.path.join(dest_dir_path, relative_path.replace(".md", ".html"))
            generate_page(entry_path, template_path, new_dest_path)
        if os.path.isdir(entry_path):
            new_dest_path = os.path.join(dest_dir_path, relative_path)
            generate_pages_recursive(entry_path, template_path, new_dest_path)
