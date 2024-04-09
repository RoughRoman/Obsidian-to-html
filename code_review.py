import sys, os
from openai import OpenAI
import requests
import json

print("started")

code = sys.stdin.read()

client = OpenAI(
    api_key = os.getenv('OPENAI_KEY')
)

print("envs:")
email = os.getenv('EMAIL')
name = os.getenv('NAME')
lang = os.getenv('LANG')
user_model = os.getenv('MODEL')
custom_instructions = os.getenv('CUSTOM_INSTRUCTIONS')
callback_url = os.getenv('CALLBACK')
print(email,name,lang,user_model,custom_instructions,callback_url)
print('/n')

response = client.chat.completions.create(
  model=user_model,
  messages=[
    {"role": "system", "content": f"You are an experienced {lang} Programmer who will review the following code. Look for potential errors and bad style for {lang} as well as any custom standards supplied before the code. Do not rewrite any code. Supply a list of recommended changes in plain english. Also supply a short summary of what the code does. "},
    {"role": "user", "content": f"Here are the standards if supplied: {custom_instructions}. Here is the {code}"}
  ]
)


print("Ready to send")

payload = {"email":f"{email}","name":f"{name}","message":f"{str(response.choices[0].message)}"}
print(payload)
print(requests.post(callback_url, json = json.dumps(payload)))

print("end")

