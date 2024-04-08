# analyze_code_changes.py

import os
import sys
import requests
import openai

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Read code from standard input
code = sys.stdin.read()

# Prompt for OpenAI analysis
prompt = os.getenv("PROMPT") + "\nCode of commit is:\n```\n" + code + "\n```"
if len(prompt) > int(os.getenv("MAX_LENGTH")):
    print(f"Prompt too long for OpenAI: {len(prompt)} characters, "
          f"sending only first {os.getenv('MAX_LENGTH')} characters")
    prompt = prompt[:int(os.getenv("MAX_LENGTH"))]

# Request analysis from OpenAI
response = openai.ChatCompletion.create(
    model=os.getenv("MODEL"),
    messages=[
        {"role": "system", "content": "You are a helpful assistant and code reviewer."},
        {"role": "assistant", "content": "You are code reviewer for a project."},
        {"role": "user", "content": prompt},
    ],
)

if response.choices:
    review_text = response.choices[0].message.strip()
else:
    review_text = f"No correct answer from OpenAI!\n{response}"

# Send review_text to another API
url = "https://your-api-endpoint.com"
data = {"review": review_text}

# Using the requests library to send the data to another API
try:
    r = requests.post(url, json=data)
    r.raise_for_status()
    print(f"Response from API: {r.status_code}")
except requests.exceptions.HTTPError as err:
    print(f"Error: {err}")
