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

format = """
    {
    "Introduction": "00:00:00",
    "Deep Learning": "00:25:12"
    }
"""
def generate_timestamps(description):
    start_time = timer()
    timestamp_response = ollama.generate(model="llama3:8b",
                                         format="json",
                                         stream=False,
                                         prompt=f"Extract all the values that are in the same format {format} . Look through the text to find it. {description}. Respond in JSON format.")

    timestamp_json_str = timestamp_response.model_dump_json()

    timestamp_json = json.loads(timestamp_json_str)
    end_time = timer()
    print(timestamp_json['response'])
    print(f"Time taken to generate timestamp: {end_time-start_time}")

import re

def extract_chapters(description):
  # Regex pattern to match the time and chapter
  pattern = r"(?P<time>(?:\d{1,3}:)*\d{1,2}:\d{1,2})[- )]*(?P<chapter>.*)"
  # Extracting matches into a dictionary
  matches = re.findall(pattern, description, re.MULTILINE)
  chapter_dict = {time: chapter for time, chapter in matches}
  print(chapter_dict)
  return chapter_dict
# generate_timestamps(description=text)
extract_chapters(texts)

