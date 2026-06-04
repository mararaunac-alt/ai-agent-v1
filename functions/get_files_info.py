import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    #Validate the directory is within the working directory
    try:

        absolute_path_working_directory = os.path.abspath(working_directory)
        full_path_to_target_directory = os.path.normpath(os.path.join(absolute_path_working_directory, directory))

        # Will be True or False
        valid_target_dir = os.path.commonpath([absolute_path_working_directory, full_path_to_target_directory]) == absolute_path_working_directory

        if not valid_target_dir:
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        
        if not os.path.isdir(full_path_to_target_directory):
            return f'Error: "{directory}" is not a directory'
    
        # List files and directories in the target directory
        list_files = ""
        for item in os.listdir(full_path_to_target_directory):
            item_path = os.path.join(full_path_to_target_directory, item)
            if  os.path.isdir(item_path):
                list_files += f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir=True\n"
            else:
                list_files += f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir=False\n"
        return list_files.strip()
    
    except Exception as e:
        return f"Error: {e}"
