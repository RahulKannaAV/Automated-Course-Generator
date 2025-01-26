import re
import regex
import json


def get_summary_json(text):
    json_pattern = r'{(?:[^{}]|(?R))*}'

    # Search for JSON using `regex` module
    match = regex.search(json_pattern, text, regex.DOTALL)

    if match:
        json_str = match.group()

        # Parse the JSON string into a Python object
        try:
            json_obj = json.loads(json_str)
            print("\nParsed JSON object:")
            return(json.dumps(json_obj, indent=2))
        except json.JSONDecodeError as e:
            print("\nInvalid JSON:", e)
            return {}
    else:
        print("No JSON found in the string.")
        return {}
