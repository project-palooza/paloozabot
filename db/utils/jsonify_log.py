# getting GPT to organize as json
import json
import openai
from dotenv import load_dotenv,find_dotenv
import os

_ = load_dotenv(find_dotenv())
api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

with open('utils/log_extraction_prompt.md','r') as f:
    base_prompt = f.read()

base_prompt = base_prompt.replace("\n"," ")

def tag_db(log_json):
    if len(log_json) == 5:
        table_name = "System"
    elif len(log_json) == 3:
        table_name = "Command"
    elif len(log_json) == 7:
        table_name = "Message"
    else:
        table_name = "error"
        print(f"there was a mistake in parsing the log, there's {len(log_json)} fields\n")
        print(log_json)
    return table_name

def jsonify_log(log,prompt=base_prompt, model="gpt-4"):
    '''basic completion from gpt4'''
    to_json = prompt.format(log=log)
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

    db_name = tag_db(output)

    return {"db_name":db_name, "data":output}

