import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables")
        exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "prompt",
        nargs="?",  # optional positional argument
        default="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        help="User prompt",
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    user_prompt = args.prompt
    verbose = args.verbose

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    print(response.text)

    usage = response.usage_metadata
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")

if __name__ == "__main__":
    main()
