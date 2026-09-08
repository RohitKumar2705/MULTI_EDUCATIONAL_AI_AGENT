from openai import OpenAI

from config.settings import MODEL_NAME, client


def run_evaluator_agent(
    question: str,
    tutor_answer: str
):

    prompt = f"""
You are the Evaluator Agent in a multi-agent
educational AI system.

Student Question:

{question}

Tutor Answer:

{tutor_answer}

Evaluate the answer.

Return:

1. Correctness score from 1 to 10
2. Completeness score from 1 to 10
3. Clarity score from 1 to 10
4. Problems found
5. Suggestions for improvement
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You evaluate educational answers carefully."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content