import os
import shutil
from generatecontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def clear_directory(path):
    """Delete all contents inside the directory but not the directory itself."""
    if not os.path.exists(path):
        return
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            shutil.rmtree(full_path)
            print(f"Deleted directory: {full_path}")
        else:
            os.remove(full_path)
            print(f"Deleted file: {full_path}")

def copy_recursive(src, dst):
    """
    Recursively copies all contents from src directory to dst directory.
    First clears the destination directory.
    """
    if not os.path.exists(src):
        raise ValueError(f"Source directory does not exist: {src}")

    # Clear destination directory
    if os.path.exists(dst):
        clear_directory(dst)
    else:
        os.makedirs(dst)
        print(f"Created destination directory: {dst}")

    def copy_all(src_dir, dst_dir):
        for item in os.listdir(src_dir):
            s_path = os.path.join(src_dir, item)
            d_path = os.path.join(dst_dir, item)
            if os.path.isdir(s_path):
                os.makedirs(d_path, exist_ok=True)
                print(f"Created directory: {d_path}")
                copy_all(s_path, d_path)  # recursive call
            else:
                shutil.copy2(s_path, d_path)
                print(f"Copied file: {s_path} -> {d_path}")

    copy_all(src, dst)

def main():
    copy_recursive('static', 'public')

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)
main()