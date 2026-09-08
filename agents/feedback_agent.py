from openai import OpenAI

from config.settings import MODEL_NAME, client


def run_feedback_agent(
    tutor_answer: str,
    evaluation: str
):

    prompt = f"""
You are the Feedback Agent.

Tutor Answer:

{tutor_answer}

Evaluator Feedback:

{evaluation}

Create constructive feedback.

Explain:

1. What was done well
2. What can be improved
3. What the student should learn next
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You provide constructive educational feedback."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content