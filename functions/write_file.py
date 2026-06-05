import os
from google.genai import types

def write_file(working_directory: str, file_path: str, content: str) -> str:

    try:
        absolute_path_working_directory = os.path.abspath(working_directory)
        full_path_to_target_file = os.path.normpath(os.path.join(absolute_path_working_directory, file_path))

        # Validate the file is within the working directory
        valid_target_file = os.path.commonpath([absolute_path_working_directory, full_path_to_target_file]) == absolute_path_working_directory

        if not valid_target_file:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if os.path.isdir(full_path_to_target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        # Ensure the target directory exists
        target_dir = os.path.dirname(full_path_to_target_file)
        os.makedirs(target_dir, exist_ok=True)

        # Write content to the file
        with open(full_path_to_target_file, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {e}"

# Define the function schema(definition) for write_file
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory, creating the file if it does not exist and ensuring it does not write outside the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to write content to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file",
            )
        },
        required=["file_path", "content"]
    )
)
