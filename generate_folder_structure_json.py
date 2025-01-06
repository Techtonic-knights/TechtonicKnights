import os
import json
import re

def extract_readme_data(subfolder_path):
    """Extracts problem name and YouTube link from a subfolder's README.md."""
    readme_path = os.path.join(subfolder_path, "README.md")
    
    if not os.path.exists(readme_path):
        print(f"README.md not found in {subfolder_path}, skipping...")
        return None, None, None
    
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


def extract_readme_data_for_non_lc(subfolder_path):
    """Extracts YouTube link from a subfolder's README.md (for non-lc)."""
    readme_path = os.path.join(subfolder_path, "README.md")

    if not os.path.exists(readme_path):
        print(f"README.md not found in {subfolder_path}, skipping...")
        return None

    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    # Regex to extract YouTube link
    youtube_match = re.search(r'\[!\[Click to Play\]\(https://img\.youtube\.com/vi/([^/]+)', readme_content)
    if youtube_match:
        return f"https://www.youtube.com/watch?v={youtube_match.group(1)}"
    return None


def get_folder_structure(path, ignored_folders=None):
    if ignored_folders is None:
        ignored_folders = {'.git', '.ipynb_checkpoints'}  # Default ignored folders

    folder_structure = {}
    non_lc_folders = ["LLM Projects"]

    # Walk the directory structure
    for root, dirs, files in os.walk(path):
        # Skip ignored folders
        dirs[:] = [d for d in dirs if d not in ignored_folders]
        
        # Skip processing subfolders if README.md exists in the folder (but not for the root)
        if root != path and 'README.md' in files:
            # If README.md exists, do not traverse subfolders
            dirs[:] = []  # Clear the dirs list to prevent walking into subdirectories
        
        # Classify the first-level directories as lc and non_lc
        if root == path:  # We're at the root folder
            for dir in dirs:
                # Assume all directories other than the ones in `non_lc` list are lc
                folder_structure[dir] = {}
                if dir in non_lc_folders:
                    non_lc_folders.append(dir)
        else:
            # Get relative path from the root folder
            relative_path = os.path.relpath(root, path)
            # Split the path to get the nested structure
            subfolders = relative_path.split(os.sep)
            
            # Traverse down the nested structure to add new subdirectories
            current_structure = folder_structure
            for subfolder in subfolders:
                if subfolder not in current_structure:
                    current_structure[subfolder] = {}
                current_structure = current_structure[subfolder]

            # If the current folder has a README.md, extract the necessary data
            if 'README.md' in files:
                problem_name, problem_link, youtube_link = extract_readme_data(root)

                # If it's a lc folder
                if problem_name and problem_link and youtube_link:
                    current_structure.update({
                        "problem_name": problem_name,
                        "problem_link": problem_link,
                        "youtube_link": youtube_link,
                    })
                else:  # Otherwise, treat it as non-lc and extract only the YouTube link
                    youtube_link = extract_readme_data_for_non_lc(root)
                    if youtube_link:
                        current_structure.update({
                            "youtube_link": youtube_link
                        })

    return folder_structure


# Get the current directory
current_directory = os.getcwd()

# Generate the folder structure, ignoring specific folders
folder_structure = get_folder_structure(current_directory)

# Convert to JSON string
json_string = json.dumps({os.path.basename(current_directory): folder_structure}, indent=2)

# Write the JSON string to a file
with open('folder_structure.json', 'w') as json_file:
    json_file.write(json_string)

print("Folder structure has been written to 'folder_structure.json'")

