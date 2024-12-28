from markdown_blocks import markdown_to_html_node
# from htmlnode import ParentNode
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print ("Generating page from " + from_path + " to " + dest_path + " using  " + template_path)

    file = open(from_path, "r")
    file_content = file.read()
    file.close()

    file = open(template_path, "r")
    template_content = file.read()
    file.close()

    new_content = markdown_to_html_node(file_content)
    title = extract_title(file_content)
    output = template_content.replace("{{ Title }}", title).replace("{{ Content }}", new_content.to_html())
   
    path_parts = dest_path.split("/")
    dest_dir = "/".join(path_parts[:-1])
    # print(dest_dir)
    if (not os.path.exists(dest_dir)):
        os.makedirs(dest_dir)

    file = open(dest_path, "w")
    file.write(output)
    file.close()
    
    # print(dest_path)
    # return output

