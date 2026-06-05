import os
from config import max_characters
from google.genai import types

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
    

# Define the function schema(definition) for get_file_content
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a specified file relative to the working directory, with a maximum character limit to prevent excessively long outputs",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to read content from, relative to the working directory",
            ),
        },
        required=["file_path"]
    ),
)

