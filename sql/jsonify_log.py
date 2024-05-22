# getting GPT to organize as json
import json
import openai
from dotenv import load_dotenv,find_dotenv
import os

_ = load_dotenv(find_dotenv())
api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

with open('log_extraction_prompt.md','r') as f:
    base_prompt = f.read()

base_prompt = base_prompt.replace("\n"," ")

def jsonify_log(log,prompt=base_prompt, model="gpt-4"):
    '''basic completion from gpt4'''
    to_json = base_prompt.format(log=log)
    messages = [{"role": "user", "content": to_json}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, 
    )
    try:
        output = json.loads(response.choices[0].message["content"])
    except:
        output = {}
        print("there was a problem converting to json. empty dictionary returned")

    return output

