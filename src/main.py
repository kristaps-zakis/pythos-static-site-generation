

import os
import shutil
from generate_page import generate_page

source_folder = 'static'
target_folder = 'public'

def ___main___():
    if (not os.path.exists(target_folder)):
        os.makedirs(target_folder)

    copy_files(source_folder, target_folder)

    generate_page("./content/index.md", "./template.html", "./public/index.html")


def copy_files(source_folder, target_folder):
    delete_files(target_folder)

    copy_items(source_folder, target_folder)

def copy_items(source_folder, target_folder):   
    print("SF", source_folder)
    for file in os.listdir(source_folder):
        source_element = source_folder + "/" + file
        if not os.path.isfile(source_element):
            os.makedirs(target_folder + "/" + file)
            copy_items(source_element, target_folder + "/" + file)
        if os.path.isfile(source_element):
            print(source_element, "||", target_folder + "/" + file)
            shutil.copy(source_element, target_folder + "/" + file)
            
def delete_files(dir):
    for file in os.listdir(dir):
        if os.path.isfile(dir +"/" + file):
            os.remove(dir +"/" + file)
        else:
            delete_files(dir +"/" + file)
            os.rmdir(dir +"/" + file)

if __name__ == "__main__":
    ___main___()

