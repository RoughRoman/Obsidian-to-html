import sys, os
from openai import OpenAI
import requests

code = sys.stdin.read()

client = OpenAI(
    api_key = os.getenv('OPENAI_KEY')
)

email = os.getenv('EMAIL')
name = os.getenv('NAME')

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an experienced Programmer who will review the following code."},
    {"role": "user", "content": f"{code}"}
  ]
)

api_url = 'https://prod-66.westeurope.logic.azure.com:443/workflows/867f215910024d3a8d8623eb0b4dc8e4/triggers/manual/paths/invoke?api-version=2016-06-01'

response = requests.post(api_url, data=response)

print(response.text)
