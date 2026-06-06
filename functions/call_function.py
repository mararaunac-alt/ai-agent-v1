from google.genai import types
from .get_files_info import schema_get_files_info, get_files_info
from .get_file_content import schema_get_file_content, get_file_content
from .write_file import schema_write_file, write_file
from .run_python_file import run_python_file, schema_run_python_file
from collections.abc import Callable


# Define the available functions that the model can call, including their schemas and descriptions. This will allow the model to understand what functions it can call and how to use them
available_functions = types.Tool(
    function_declarations=[schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file],
)

# Create a mapping of function names to their corresponding Python function implementations, which will be used to route the function calls from the model to the correct implementation when the model decides to call a function. This mapping will allow us to easily look up and execute the correct function based on the function name provided by the model in its function call.
function_map: dict[str, Callable[..., str]] = {
    "get_file_content": get_file_content,
    "write_file": write_file,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
}

# Define a function to handle the function calls from the model, which will execute the corresponding Python functions based on the function name and arguments provided by the model. This function will be responsible for routing the function calls to the correct implementation and returning the results back to the model.
def call_function(
    function_call: types.FunctionCall, verbose: bool = False
) -> types.Content:
    
    # Print the function call details for debugging purposes, including the function name and arguments, if the verbose flag is set to True. This will help us understand what function calls are being made by the model and with what arguments, which can be useful for debugging and improving the model's behavior.
    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")

    # Look up the function in the function map and execute it with the provided arguments, handling any errors that may occur during execution and returning the results in a format that can be sent back to the model as a response to the function call.
    function_name = function_call.name or ""
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    # Convert the function call arguments from the model into a dictionary format that can be passed to the Python function implementations. This will allow us to easily extract the necessary parameters from the function call and pass them to the corresponding Python functions for execution.
    args = dict(function_call.args) if function_call.args else {}
    args["working_directory"] = "./calculator"
    
    # Execute the function and capture the result, handling any exceptions that may occur during execution and returning the results in a structured format that can be sent back to the model as a response to the function call. This will allow us to provide feedback to the model about the success or failure of the function execution, as well as any relevant output or error messages.
    function_result = function_map[function_name](**args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
