import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:

        absolute_path_working_directory = os.path.abspath(working_directory)
        full_path_to_target_directory = os.path.normpath(os.path.join(absolute_path_working_directory, directory))

        # Will be True or False
        valid_target_dir = os.path.commonpath([absolute_path_working_directory, full_path_to_target_directory]) == absolute_path_working_directory

        if not valid_target_dir:
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        
        if not os.path.isdir(full_path_to_target_directory):
            return f'Error: "{directory}" is not a directory'
        
        return f'Success: "{directory}" is within the working directory'
    
    except Exception as e:
        return f"Error: {e}"
