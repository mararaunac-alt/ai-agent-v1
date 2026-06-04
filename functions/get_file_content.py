import os
from config import max_characters

def get_file_content(working_directory: str, file_path: str) -> str:
    
    try:
        absolute_path_working_directory = os.path.abspath(working_directory)
        full_path_to_target_file = os.path.normpath(os.path.join(absolute_path_working_directory, file_path))

        # Validate the file is within the working directory
        valid_target_file = os.path.commonpath([absolute_path_working_directory, full_path_to_target_file]) == absolute_path_working_directory

        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(full_path_to_target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # Read the file content with a maximum character limit
        with open(full_path_to_target_file, 'r') as f:
            file_content_string = f.read(max_characters)
            if f.read(1):  # Check if there's more content after reading max_characters
                file_content_string += f'[...File "{file_path}" truncated at {max_characters} characters]'
            return file_content_string
    
    except Exception as e:
        return f"Error: {e}"