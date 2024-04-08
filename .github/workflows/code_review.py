import sys, os
import openai
import requests

# Read the code changes from standard input
code = sys.stdin.read()

# Define your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define the email and name of the pull request sender
email = os.getenv('EMAIL')
name = os.getenv('NAME')

# Perform the OpenAI request
response = openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt=f"Pull request from {name} ({email}) containing the following code changes:\n```{code}```",
    max_tokens=100
)

# Define the URL of the second API
api_url = 'YOUR_SECOND_API_URL'

# Send the OpenAI response to the second API
response = requests.post(api_url, data=response)

# Handle the response from the second API as needed
print(response.text)
