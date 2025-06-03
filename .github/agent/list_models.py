import requests
import os
import sys

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY is not set in environment variables.", file=sys.stderr)
        sys.exit(1)

    url = "https://generativelanguage.googleapis.com/v1beta/models"
    params = {"key": api_key}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        models = data.get("models", [])
        if not models:
            print("No models found.")
            sys.exit(0)
        print("Available models:")
        for model in models:
            print(f"- {model.get('name', 'unnamed')}")
        first_model = models[0].get("name", "")
        print(f"::set-output name=model::{first_model}")
    except requests.RequestException as e:
        print(f"Error querying the API: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()