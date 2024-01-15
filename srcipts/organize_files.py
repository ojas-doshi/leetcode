import os
import re
import shutil
import logging

class FolderOrganizer:
    def __init__(self, root_folder='.'):
        self.root_folder = os.path.abspath(root_folder)
        self.readme_file = 'README.md'
        self.difficulty_pattern = r"</h2><h3>(\w+)</h3><hr>"
        self.src_default_path = 'src'
        self.difficulty_levels = ['easy', 'medium', 'hard']

        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def extract_difficulty_level(self, file_path):
        """Extract difficulty level from the README file."""
        with open(file_path, 'r') as file:
            content = file.read()
            match = re.search(self.difficulty_pattern, content)
            return match.group(1) if match else None

    def check_in_previous_solutions(self, folder_name):
        """Check if the folder exists in previous solutions."""
        for level in self.difficulty_levels:
            if os.path.exists(os.path.join(self.root_folder, self.src_default_path, level, folder_name)):
                return True, level
        return False, None

    def organize_folders_by_difficulty(self):
        """Organize folders based on difficulty levels."""
        for folder_name in os.listdir(self.root_folder):
            folder_path = os.path.join(self.root_folder, folder_name)
            if os.path.isdir(folder_path):
                readme_path = os.path.join(folder_path, self.readme_file)
                exists_in_previous, difficulty_level = self.check_in_previous_solutions(folder_name)

                # Determine difficulty level based on README or previous solutions
                difficulty_level = difficulty_level or (exists_in_previous and 'easy')
                if difficulty_level:
                    difficulty_folder = os.path.join(self.root_folder, self.src_default_path, difficulty_level.lower())
                    os.makedirs(difficulty_folder, exist_ok=True)
                    shutil.move(folder_path, os.path.join(difficulty_folder, folder_name))

                    # Logging the movement of folders
                    self.logger.info(f"Moved '{folder_name}' to '{difficulty_folder}' folder.")
                else:
                    # Logging if no difficulty level is found
                    self.logger.warning(f"No difficulty level found for '{folder_name}'.")

# Example usage
if __name__ == "__main__":
    organizer = FolderOrganizer()
    organizer.organize_folders_by_difficulty()
