import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    try:
        absolute_path_working_directory = os.path.abspath(working_directory)
        full_path_to_target_file = os.path.normpath(os.path.join(absolute_path_working_directory, file_path))

        # Validate the file is within the working directory
        valid_target_file = os.path.commonpath([absolute_path_working_directory, full_path_to_target_file]) == absolute_path_working_directory

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(full_path_to_target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        # Run the Python file and capture its output
        command = ["python", full_path_to_target_file]
        if args:
            command.extend(args)
        
        result = subprocess.run(command, cwd=absolute_path_working_directory, capture_output=True, text=True, timeout=30)
        
        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        if not result.stderr and not result.stdout:
            return f"No output produced"
        else:
            return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"

        return result.stdout
    
    except Exception as e:
        return f"Error: executing Python file: {e}"