import ollama
import json
from timeit import default_timer as timer

def generate_quiz(query):
  start = timer()
  print("Generating....")
  response_generated = ollama.generate(format="json",
                                       model="llama3:8b",
                                       stream=False,
                                       prompt=f"Generate summary for {query} concepts in JSON response")
  print("Generated successfully.")

  json_response = json.loads(response_generated.model_dump_json())

  print(json_response['response'], type(json_response))
  end = timer()

  print(f"Total time taken: {end-start} seconds")
generate_quiz("Hello World in Rust")