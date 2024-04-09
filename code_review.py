import sys, os
from openai import OpenAI
import requests

# Read the code changes from standard input
code = sys.stdin.read()

# Define your OpenAI API key
client = OpenAI(
    api_key = os.getenv('OPENAI_KEY')
)

# Define the email and name of the pull request sender
email = os.getenv('EMAIL')
name = os.getenv('NAME')

# Perform the OpenAI request
response = client.completions.create(
    model="gpt-3.5-turbo",
    prompt=f"Please Review the following Pull request from {name} ({email}) containing the following code changes:\n```{code}```",
    max_tokens=4000
)

# Define the URL of the second API
api_url = 'https://prod-66.westeurope.logic.azure.com:443/workflows/867f215910024d3a8d8623eb0b4dc8e4/triggers/manual/paths/invoke?api-version=2016-06-01'

# Send the OpenAI response to the second API
response = requests.post(api_url, data=response)

# Handle the response from the second API as needed
print(response.text)
