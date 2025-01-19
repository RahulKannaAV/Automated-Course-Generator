import ollama
import re
import json
import ast

# Just run the docker instance and then try to run the functions
# Command: docker exec -it ollama ollama run llama3:8b


def generate_quiz(query):

    ollama.pull('llama3:8b')
    response = ollama.chat(model='llama3:8b', messages=[
      {
        'role': 'user',
        'content': f'Generate 5 quiz questions, 4 options related to this in JSON format which should also contain answers field. {query}',

      },
      ], stream=True)

    results = ""
    for chunk in response:
      print(chunk['message']['content'], end='', flush=True)
      results += chunk['message']['content']


    questions_json = extract_json(results)
    # Extracted JSON
    print(questions_json[0])

    # Save it to the Database


def get_important_keywords(paragraph):
    ollama.pull('llama3:8b')

    response = ollama.chat(model='llama3:8b', messages=[{
        "role": "user",
        "content": f"Extract important keywords from the given paragraph. Present it in python list format in a single line. {paragraph}"
    }], stream=True)

    generated_text = ""
    for idx, chunk in enumerate(response):
        print(chunk['message']['content'], end='', flush=True)
        generated_text += chunk['message']['content']


    filtered_list = extract_list(generated_text)
    return filtered_list

def extract_json(output):
    pattern = r"```(.*?)```"
    match = re.search(pattern, output, re.DOTALL)

    if match:
        json_text = match.group(1).strip()
        try:
          # Parse the JSON
          questions = json.loads(json_text)
          print("JSON extracted successfully")
          return questions
        except json.JSONDecodeError as e:
          print(f"Error decoding JSON: {e}")
          return []
    else:
        print("No JSON block found in the text.")
        return []

def extract_list(text):
    # Regular expression to match a Python list
    pattern = r"\[.*?\]"

    # Find all matches
    matches = re.findall(pattern, text)

    # Extract and split into individual elements
    individual_elements = []
    for match in matches:
        # Safely evaluate the matched string into a Python list
        parsed_list = ast.literal_eval(match)

        # Extend the elements into the result list
        individual_elements.extend(parsed_list)

    return individual_elements

"""with open('../big_lesson.txt', 'r') as f:
    generate_quiz(f.read())"""

with open("../big_lesson.txt", 'r') as f:
    keywords = get_important_keywords(f.read())

print("Here bro: ", keywords)

