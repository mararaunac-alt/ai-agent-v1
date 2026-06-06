import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions, call_function
from helper_function_response_handler import handle_function_response
import sys

def main():

    #Parse user input first
    parser = argparse.ArgumentParser(description="Ask Gemini a question from the command line")
    parser.add_argument("user_prompt", type=str, help="The message to send to Gemini")
    #Add an optional verbose flag to print additional information about the API response
    parser.add_argument("--verbose", action="store_true", help="Print additional information about the API response")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`

    #Load config/secrets
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")
    
    #Set up the client
    client = genai.Client(api_key=api_key)

    #Wrap prompt in Content/Part structure to support text, images, and other media types
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    """""
    Iteratively call the API, allowing the model to call functions and update the conversation with the function results 
    until we reach a stopping condition (e.g., a certain number of function calls, or a specific response 
    from the model indicating that it is done)
    """
    for call in range(20):

        #Make the API call
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=messages,
            config=types.GenerateContentConfig(system_instruction=system_prompt, tools=[available_functions])
            )
        if response.usage_metadata is None:
            raise RuntimeError("Response usage metadata is None")
        
        #Extract the model's response and append it to the conversation history for the next API call.
        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)
        
        #Handle if the verbose flag is set to print additional information about the API response
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        
        
        #Handle the response
        response_list = []
    
        #Check if the model has made any function calls in its response, and if so, execute those and append the results to the conversation history.
        if response.function_calls:
            for function_call in response.function_calls:
                function_response = call_function(function_call)
                helper_function_response = handle_function_response(function_response, verbose=args.verbose)
                response_list.append(helper_function_response)
            messages.append(types.Content(role="user", parts=response_list))

        else: 
            print(response.text)
            break
    else:
        print("Reached maximum number of function calls. Ending conversation.")
        sys.exit(1)


if __name__ == "__main__":
    main()
