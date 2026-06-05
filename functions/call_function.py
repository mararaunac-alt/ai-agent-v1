from google.genai import types
from .get_files_info import schema_get_files_info
from .get_file_content import schema_get_file_content
from .write_file import schema_write_file
from .run_python_file import schema_run_python_file

# Define the available functions that the model can call, including their schemas and descriptions. This will allow the model to understand what functions it can call and how to use them
available_functions = types.Tool(
    function_declarations=[schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file],
)

