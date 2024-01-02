import os
import re
import shutil

# Read README.md file
readme_file = 'README.md'
difficulty_pattern = r"</h2><h3>(\w+)</h3><hr>"  # Assuming the difficulty level is mentioned in the README.md

src_default_path = 'src'

# Function to extract difficulty level from README.md
def extract_difficulty_level(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        match = re.search(difficulty_pattern, content)
        if match:
            return match.group(1)
        else:
            return None

# Function to move folders to the respective difficulty level folder
def organize_folders_by_difficulty(root_folder):
    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            readme_path = os.path.join(folder_path, readme_file)
            if os.path.exists(readme_path):
                difficulty_level = extract_difficulty_level(readme_path)
                if difficulty_level:
                    difficulty_folder = os.path.join(root_folder,"src", difficulty_level)
                    difficulty_folder = difficulty_folder.lower()
                    if not os.path.exists(difficulty_folder):
                        os.makedirs(difficulty_folder)
                    shutil.move(folder_path, os.path.join(difficulty_folder, folder_name))
                    print(f"Moved '{folder_name}' to '{difficulty_folder}' folder.")

# Replace 'root_folder' with the path to your main directory containing the problem folders
root_folder = os.path.curdir
organize_folders_by_difficulty(root_folder)
