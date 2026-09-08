import sys
from pathlib import Path 
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(str(BASE_DIR))

from agents.tutor_agent import run_tutor_agent 
from agents.planner_agent import run_planner_agent 
from agents.evaluator_agent import run_evaluator_agent 
from agents.feedback_agent import run_feedback_agent 

def run_multi_agent_system(question):
    print("student question")
    print(question)

    # planner
    print("running planner agent")
    learning_plan = run_planner_agent(question)
    # print("learning plan")
    print(learning_plan)

    # tutor
    print(" runnung tutor agent")
    tutor_answer = run_tutor_agent(question,learning_plan)
    print(tutor_answer)


    # evaluator
    print("running evaluator agent")
    evaluation = run_evaluator_agent(
        question,
        tutor_answer
    )

    print(evaluation)

    # feedback 
    print("\nRunning Feedback Agent...\n")

    feedback = run_feedback_agent(
        tutor_answer,
        evaluation
    )

    print(feedback)

    return {
        "question":question,
        "learning_plan":learning_plan,
        "tutor_answer":tutor_answer,
        "evaluation":evaluation,
        "feedback":feedback

                }


if __name__ == "__main__":
    question = """
Explain Support Vector Machines
to a beginner.
"""

    result = run_multi_agent_system(
        question
    )