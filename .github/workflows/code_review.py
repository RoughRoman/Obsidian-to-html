import sys, os
from openai import OpenAI
import requests
import json

code = sys.stdin.read()

client = OpenAI(
    api_key = os.getenv('OPENAI_KEY')
)

try:
    # attempt to parse json config
    with  open("./config.json","r") as config_file:
      parsed_file = json.loads(config_file.read())
      email = parsed_file["reviewer_email"]
      name = parsed_file["name"]
      lang = parsed_file["lang"]
      user_model = parsed_file["model"]
      custom_standards = parsed_file["custom_standards"]
      callback_url = parsed_file["response_callback_url"]

except:
  print("Couldn't read config.json. Defaulting to main.yml env variables.")
  # fall back on default env variables in yml file
  email = os.getenv('EMAIL')
  name = os.getenv('NAME')
  lang = os.getenv('LANG')
  user_model = os.getenv('MODEL')
  custom_standards = os.getenv('CUSTOM_INSTRUCTIONS')
  callback_url = os.getenv('CALLBACK')



response = client.chat.completions.create(
  model=user_model,
  messages=[
    {"role": "system", "content": f"You are an experienced {lang} Programmer who will review the following code. Look for potential errors and bad style for {lang} as well as any custom standards supplied before the code. Do not rewrite any code. Supply a list of recommended changes in plain english. Also supply a short summary of what the code does. "},
    {"role": "user", "content": f"Here are the standards if supplied: {custom_standards}. Here is the {code}"}
  ]
)

payload = json.dumps({
  "email": email,
  "name": name,
  "message": str(response.choices[0].message.content)
})
headers = {
  'Content-Type': 'application/json'
}

requests.request("POST", callback_url, headers=headers, data=payload)

