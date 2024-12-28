from markdown_blocks import markdown_to_html_node
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
    if (not os.path.exists(dest_dir)):
        os.makedirs(dest_dir)


    dest_dir = "/".join(path_parts[:-1]) + "/index.html"
    file = open(dest_dir, "w")
    file.write(output)
    file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        source_element = dir_path_content + "/" + file
        if not os.path.isfile(source_element):
            generate_pages_recursive(source_element, template_path, dest_dir_path + "/" + file)
        if os.path.isfile(source_element):
            generate_page(source_element, template_path, dest_dir_path + "/" + file)
