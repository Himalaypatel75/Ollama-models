import requests

# Define the API endpoint and the model you want to use
base_url = "http://localhost:11434"
model_name = "mario"
endpoint = f"{base_url}/api/generate"

# Define the prompt template
template = """Question: {question}

Answer: Let's think step by step."""

# Create the prompt using the template
def create_prompt(question):
    return template.format(question=question)

# Define the function to invoke the model via API
def invoke_model(question):
    prompt = create_prompt(question)
    payload = {
        "model": model_name,
        "prompt": prompt,
        "max_tokens": 150  # You can adjust the max tokens as per your requirement
    }
    
    # Send the request to the API
    response = requests.post(endpoint, json=payload)
    
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        raise ValueError(f"API call failed with status code {response.status_code}: {response.text}")

# Example usage
question = "What is LangChain?"
answer = invoke_model(question)
print(answer)
