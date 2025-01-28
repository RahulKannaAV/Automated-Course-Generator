import ollama
import json
from timeit import default_timer as timer
from flask import current_app as app

def generate_quiz(topic, spoken_content):
    start_time = timer()
    with app.open_resource('static/quiz_obj.json') as f:
        json_data = json.load(fp=f)
        print(f"Template loaded. Generating....")
        response = ollama.generate(model="llama3:8b",
                               format="json",
                               prompt=f"Generate 5 quiz questions of balanced difficulty level for the topic {topic}, as well as attached lecture captions {spoken_content}, on the basis of this template {json_data}. Respond in JSON format and make sure it is related to the lectures.")

        quiz_metadata = json.loads(response.model_dump_json())

        quiz_data = json.loads(quiz_metadata['response'])
        print("Quiz questions generated successfully.")
    end_time = timer()

    print(f"Total time taken: {end_time - start_time} seconds")
    return quiz_data["questions"]

"""with open('quiz_obj.json', 'r') as f:
    json_data = json.load(fp=f)
    print(json_data)"""