import ollama
ollama.pull('llama3')
response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',

  },
], stream=True)

for chunk in response:
  print(chunk['message']['content'], end='', flush=True)