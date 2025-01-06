import json
import urllib.parse

# Read the JSON file
json_file_path = 'folder_structure.json'
with open(json_file_path, 'r', encoding='utf-8') as json_file:
    folder_structure = json.load(json_file)

# Function to generate the README content recursively
def generate_readme(folder_structure, level=1, path=''):
    readme_content = ""
    
    # Iterate through the folder structure
    for folder_name, folder_info in folder_structure.items():
        # Skip empty folder info
        if not folder_info:
            continue
        
        # Generate the URL for this folder, excluding the root folder name
        folder_path = f"{path}/{folder_name}" if path else folder_name
        folder_path = '' if level == 1 else folder_path
        folder_url = 'https://github.com/Techtonic-knights/TechtonicKnights/tree/main/' + urllib.parse.quote(folder_path)
        
        # Create heading for the current folder, making the folder name a clickable link
        readme_content += "#" * level + f" [{folder_name}]({folder_url})\n\n"
        
        # If the folder has subfolders, recurse deeper
        if isinstance(folder_info, dict):
            # If it's the penultimate folder (having subfolders with README)
            has_problem_name = any('problem_name' in subfolder_info for subfolder_info in folder_info.values())
            has_youtube_link = any('youtube_link' in subfolder_info for subfolder_info in folder_info.values()) 
            
            if has_problem_name and has_youtube_link:
                # Generate a table for the folder containing subfolders with README
                readme_content += "| Folder Name | Problem Name | YouTube Link |\n"
                readme_content += "|--------------|--------------|--------------|\n"
                for subfolder_name, subfolder_info in folder_info.items():
                    if "problem_name" in subfolder_info:
                        problem_name = subfolder_info.get("problem_name", "N/A")
                        problem_link = subfolder_info.get("problem_link", "N/A")
                        youtube_link = subfolder_info.get("youtube_link", "N/A")
                        
                        # Generate the URL for subfolders
                        subfolder_url = f"{folder_url}/{urllib.parse.quote(subfolder_name)}"
                        
                        readme_content += f"| [{subfolder_name}]({subfolder_url}) | [{problem_name}]({problem_link}) | [{youtube_link}]({youtube_link}) |\n"
                
                # Add extra newline after the table
                readme_content += "\n"
            elif has_youtube_link:
                # For non-lc folders, print the YouTube link in a table
                readme_content += "| Folder Name | YouTube Link |\n"
                readme_content += "|--------------|--------------|\n"
                for subfolder_name, subfolder_info in folder_info.items():
                    if "youtube_link" in subfolder_info:
                        youtube_link = subfolder_info.get("youtube_link", "N/A")
                        
                        # Generate the URL for subfolders
                        subfolder_url = f"{folder_url}/{urllib.parse.quote(subfolder_name)}"
                        
                        readme_content += f"| [{subfolder_name}]({subfolder_url}) | [{youtube_link}]({youtube_link}) |\n"

                # Add extra newline after the table
                readme_content += "\n"
            else:
                # Recursively process subfolders at the next level
                readme_content += generate_readme(folder_info, level + 1, folder_path)
        
        # If no subfolder, we just add a line break to separate folders
        else:
            readme_content += "\n"
    
    return readme_content

# Generate the README content
readme_content = generate_readme(folder_structure)

# Write the generated README to a file
readme_file_path = 'README.md'
with open(readme_file_path, 'w', encoding='utf-8') as readme_file:
    readme_file.write(readme_content)

print(f"README generated and saved to {readme_file_path}")

