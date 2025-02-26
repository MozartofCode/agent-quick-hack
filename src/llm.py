# @author: Aparnaa Senthilnathan, Bertan Berker, Anshul Kiyawat, Paras Jain
# ----

import os
from dotenv import load_dotenv
from pydantic import BaseModel
from openai import OpenAI

from langchain_core.messages import HumanMessage

load_dotenv()
key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

class Step(BaseModel):
    explanation: str
    output: str

class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str

def generate_summary(input, prompt):
    message = client.invoke([HumanMessage(
        content=[{"type": "text", "text": prompt},]
    )])
    return message.content





i = input("write a prompt")

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "developer", "content": [{"type":"text", "text":"You are in intelligent AI assistant specializing in converting natural language to a SQL query."}]},
        {"role": "user", "content": [{"type":"text", "text": i}]}
    ],
    response_format=MathReasoning,
)

math_reasoning = completion.choices[0].message.parsed

generate_summary(client, i)