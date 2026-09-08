from openai import OpenAI

from config.settings import MODEL_NAME, client


def run_tutor_agent(
    question: str,
    learning_plan: str
):

    prompt = f"""
You are the Tutor Agent.

Student Question:

{question}

Learning Plan:

{learning_plan}

Explain the topic clearly.

Requirements:

- Beginner friendly
- Step-by-step
- Use examples
- Explain difficult terms
- Keep the answer educational
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert educational tutor."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content