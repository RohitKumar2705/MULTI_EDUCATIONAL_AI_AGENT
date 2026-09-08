from openai import OpenAI
from config.settings import MODEL_NAME, client

def run_planner_agent(question:str):
    prompt = f"""
You are the Planner Agent in a multi-agent
educational AI system.

Student Question:
{question}

your task is to create a learning path

Return:

1. Learning objective
2. Important concepts
3. Step-by-step teaching plan
4. Example or analogy
5. Common misconceptions

Do not give the complete educational answer.

"""

    response = client.chat.completions.create(
        model = MODEL_NAME,
        messages = [
            {
            "role": "system",
                "content": (
                    "You create structured learning plans "
                    "for students."
                )
            },
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content
    




