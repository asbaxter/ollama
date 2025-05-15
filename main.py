import ollama

client = ollama.Client()

model = "gemma3:27b"  # Replace with model name
prompt = "What is python?"

response = client.generate(model=model, prompt=prompt)

print(response.response)
