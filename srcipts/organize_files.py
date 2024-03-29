import os
import re
import shutil
import logging
import filecmp

class FolderOrganizer:
    def __init__(self, root_folder='.'):
        if not os.path.isdir(root_folder):
            logging.warning("Root folder must be a valid directory.")
        self.root_folder = os.path.abspath(root_folder)
        self.readme_file = 'README.md'
        self.difficulty_pattern = r"</h2><h3>(\w+)</h3><hr>"
        self.src_default_path = 'src'
        self.difficulty_levels = ['easy', 'medium', 'hard']

        # Set up logging
        logging.basicConfig(level=logging.WARNING)
        self.logger = logging.getLogger(__name__)

    def extract_difficulty_level(self, file_path):
        """Extract difficulty level from the README file."""
        if not os.path.exists(file_path):
            self.logger.warning("File path does not exist.")
        with open(file_path, 'r') as file:
            content = file.read()
            match = re.search(self.difficulty_pattern, content)
            if match is None:
                self.logger.warning(f"No difficulty level found in {file_path}.")
            return match.group(1)

    def check_in_previous_solutions(self, folder_name):
        """Check if the folder exists in previous solutions."""
        for level in self.difficulty_levels:
            folder_path = os.path.join(self.root_folder, self.src_default_path, level, folder_name)
            if os.path.isdir(folder_path):
                if os.path.exists(folder_path):
                    return True, level
        return False, None

    def update_folder_content(self, source_dir, destination_dir):
        """Update content of the destination folder with content from the source folder."""
        if not os.path.isdir(source_dir):
            self.logger.warning(f"Source directory {source_dir} does not exist or is not a directory.")
        if not os.path.isdir(destination_dir):
            self.logger.warning(f"Destination directory {destination_dir} does not exist or is not a directory.")
        for item in os.listdir(source_dir):
            source_item_path = os.path.join(source_dir, item)
            destination_item_path = os.path.join(destination_dir, item)
            if os.path.isdir(source_item_path):
                if not os.path.exists(destination_item_path):
                    os.makedirs(destination_item_path)
                self.update_folder_content(source_item_path, destination_item_path)
            else:
                shutil.copy2(source_item_path, destination_item_path)

    def copy_folders(self, folder_name, difficulty_folder):
        """Copy folders to the specified difficulty level folder."""
        folder_path = os.path.join(self.root_folder, folder_name)
        destination_path = os.path.join(difficulty_folder, folder_name)
        if not os.path.isdir(folder_path):
            self.logger.warning(f"Source folder {folder_path} does not exist or is not a directory.")
        if os.path.exists(destination_path):
            self.logger.warning(f"Destination folder {destination_path} already exists.")
        shutil.copytree(folder_path, destination_path)
        self.logger.info(f"Copied '{folder_name}' to '{difficulty_folder}' folder.")

    def organize_folders_by_difficulty(self):
        """Organize folders based on difficulty levels."""
        for folder_name in os.listdir(self.root_folder):
            readme_path = os.path.join(self.root_folder, folder_name, self.readme_file)
            
            exists_in_previous, difficulty_level = self.check_in_previous_solutions(folder_name)
            if os.path.exists(readme_path):
                # Determine difficulty level based on README or previous solutions
                difficulty_level =  self.extract_difficulty_level(readme_path)
            
            if difficulty_level and difficulty_level.lower() not in self.difficulty_levels:
                self.logger.warning(f"Invalid difficulty level: {difficulty_level}")
            
            if difficulty_level:
                difficulty_folder = os.path.join(self.root_folder, self.src_default_path, difficulty_level.lower())
                os.makedirs(difficulty_folder, exist_ok=True)

                if os.path.exists(os.path.join(difficulty_folder, folder_name)):
                    self.update_folder_content(os.path.join(self.root_folder, folder_name), os.path.join(difficulty_folder, folder_name))
                else:
                    self.copy_folders(folder_name, difficulty_folder)
                shutil.rmtree(os.path.join(self.root_folder, folder_name))

# Example usage
if __name__ == "__main__":
    organizer = FolderOrganizer()
    organizer.organize_folders_by_difficulty()
