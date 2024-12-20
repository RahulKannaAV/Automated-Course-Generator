import ollama


def generate_quiz(query):
  ollama.pull('llama3')
  response = ollama.chat(model='llama3', messages=[
    {
      'role': 'user',
      'content': f'Generate 5 quiz questions related to this. {query}',

    },
  ], stream=True)

  for chunk in response:
    print(chunk['message']['content'], end='', flush=True)

generate_quiz("Hello World in Rust")