import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions

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
    
    #Make the API call
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt, tools=[available_functions])
        )
    if response.usage_metadata is None:
        raise RuntimeError("Response usage metadata is None")
    #Handle the response
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        if response.function_calls:
            for function_call in response.function_calls:
                print(f"Calling function: {function_call.name}({function_call.args})")
        else: 
            print(response.text)
    elif response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
