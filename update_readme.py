import os
import re

def get_subfolders(directory):
    """Recursively gets subfolders, excluding the last level."""
    subfolders = []
    for root, dirs, files in os.walk(directory, topdown=True):
        # The root is a folder, and dirs will contain its subdirectories
        # If dirs is empty, we stop the walk for that branch (it's the last level)
        if dirs:
            subfolders.append((root, dirs))
        else:
            break
    return subfolders

def write_to_markdown(md_file, content):
    """Writes content to the markdown file."""
    with open(md_file, 'a', encoding='utf-8') as f:
        f.write(content)

def extract_readme_data(subfolder_path):
    """Extracts problem name and YouTube link from a subfolder's README.md."""
    readme_path = os.path.join(subfolder_path, "README.md")
    
    if not os.path.exists(readme_path):
        print(f"README.md not found in {subfolder_path}, skipping...")
        return None, None
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Regex to extract problem name and problem link
    problem_match = re.search(r'## Problem Link\s*\[([^\]]+)\]\(([^)]+)\)', readme_content)
    if problem_match:
        problem_name = problem_match.group(1)
        problem_link = problem_match.group(2)
    else:
        problem_name, problem_link = None, None
    
    # Regex to extract YouTube link
    youtube_match = re.search(r'\[!\[Click to Play\]\(https://img\.youtube\.com/vi/([^/]+)', readme_content)
    if youtube_match:
        youtube_link = f"https://www.youtube.com/watch?v={youtube_match.group(1)}"
    else:
        youtube_link = None
    
    return problem_name, problem_link, youtube_link

def process_folders(parent_folder, md_file):
    """Processes folders recursively and writes to markdown file."""
    subfolders = get_subfolders(parent_folder)
    
    for root, dirs in subfolders:
        section_title = os.path.basename(root)  # Folder name
        section_content = f"\n## {section_title}\n"
        write_to_markdown(md_file, section_content)
        
        # Now let's check the subdirectories in the last level of this folder
        last_level_subfolders = next(os.walk(root))[1]  # Get subdirectories in the current folder
        
        table_content = "| Folder name | Problem name | YouTube Link |\n|-------------|--------------|--------------|\n"
        
        for dir_name in last_level_subfolders:
            subfolder_path = os.path.join(root, dir_name)
            # Extract problem name and YouTube link from the subfolder's README.md
            problem_name, problem_link, youtube_link = extract_readme_data(subfolder_path)
            dir_link = 'https://github.com/Techtonic-knights/TechtonicKnights/' + section_title + '/' + dir_name
            # If data exists, add it to the table
            if problem_name and youtube_link:
                table_content += f"| [{dir_name}]({dir_link}) | [{problem_name}]({problem_link}) | [{youtube_link}]({youtube_link}) |\n"
        
        # Write the table content to the markdown file
        if table_content.strip():
            write_to_markdown(md_file, table_content)

if __name__ == "__main__":
    # List of parent folders to scan (e.g., only "LeetCode")
    parent_folders_to_scan = ["LeetCode"]
    
    # Get the current working directory
    directory = os.getcwd()  # Use the current directory
    markdown_file = 'README.md'  # You can customize the markdown file name

    # Initialize the markdown file
    with open(markdown_file, 'w', encoding='utf-8') as f:
        f.write("# Folder Structure\n\n")

    # Process each parent folder in the list
    for parent_folder in parent_folders_to_scan:
        full_parent_path = os.path.join(directory, parent_folder)
        if os.path.isdir(full_parent_path):
            # Start by writing the top-level section for the folder (e.g., "LeetCode")
            # write_to_markdown(markdown_file, f"## {parent_folder}\n")
            # Process subfolders under this parent folder
            process_folders(full_parent_path, markdown_file)
        else:
            print(f"Warning: '{parent_folder}' does not exist in the current directory.")
    
    print(f"Markdown file '{markdown_file}' has been created/updated.")

