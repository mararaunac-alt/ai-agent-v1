from google import genai
from google.genai import types

def handle_function_response(function_response: genai.types.FunctionResponse, verbose: bool =False) -> str:
    """
    Handle the response from a function call made by the model
    """
    if not function_response.parts:
        raise Exception("Function call result has no parts")
    if function_response.parts[0].function_response is None:
        raise Exception("Function call result part has no function response")
    if function_response.parts[0].function_response.response is None:
        raise Exception("Function call result part has no function response content")
    
    if verbose:
        print(f"-> {function_response.parts[0].function_response.response}")
    
    return function_response.parts[0]
