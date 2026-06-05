from google.genai import types
from .get_files_info import schema_get_files_info

# Define the available functions that the model can call, including their schemas and descriptions. This will allow the model to understand what functions it can call and how to use them
available_functions = types.Tool(
    function_declarations=[schema_get_files_info],
)

