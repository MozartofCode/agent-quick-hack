# @author: Aparnaa Senthilnathan, Bertan Berker, Anshul Kiyawat, Paras Jain
# ----

import os
from dotenv import load_dotenv
from pydantic import BaseModel
from openai import OpenAI

load_dotenv()
key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def read_prompt(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

def generate_sql_query(user_input):
    prompt_1 = read_prompt('prompt_1.txt')
    response = client.ChatCompletion.create(
        model="gpt-4",  # Use the appropriate model
        messages=[
            {"role": "system", "content": prompt_1},
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']

def check_sql_vulnerability(sql_query):
    safety_prompt = read_prompt('safety_prompt.txt')
    response = client.ChatCompletion.create(
        model="gpt-4",  # Use the appropriate model
        messages=[
            {"role": "system", "content": safety_prompt},
            {"role": "user", "content": sql_query}
        ]
    )
    return response['choices'][0]['message']['content']