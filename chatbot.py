import os
import json

from dotenv import load_dotenv # type: ignore
from openai import OpenAI # type: ignore

from models import ChatResponse
from guardrails import (
    detect_pii,
    detect_prompt_injection,
    detect_off_topic
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def load_prompts():

    with open(
        "prompts.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def generate_response(user_query):

    if detect_pii(user_query):

        return {
            "error": "PII detected"
        }

    if detect_prompt_injection(user_query):

        return {
            "error": "Prompt injection detected"
        }

    if detect_off_topic(user_query):

        return {
            "error": "Off-topic query"
        }

    prompts = load_prompts()

    prompt = f"""
ROLE:
{prompts['role']}

INSTRUCTIONS:
{prompts['instructions']}

FEW SHOT EXAMPLES:
{prompts['few_shot_examples']}

USER QUERY:
{user_query}

Think step-by-step internally.

Return JSON only.

Required Fields:

intent
answer
confidence
risk_score
fraud_probability
recommendation
alerts
reasoning_summary
"""

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        response_format={
            "type": "json_object"
        },

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )

    result = response.choices[0].message.content

    data = json.loads(result)

    return ChatResponse(**data)