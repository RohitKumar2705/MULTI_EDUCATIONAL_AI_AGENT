import json
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

from agents.planner_agent import run_planner_agent
from agents.tutor_agent import run_tutor_agent
from agents.evaluator_agent import run_evaluator_agent
from agents.feedback_agent import run_feedback_agent

from monitoring.behavior_monitor import BehaviorMonitor

BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

app = FastAPI(
title="Educational Multi-Agent AI",
description=(
"Multi-agent educational system for analyzing "
"emergent behavior."
),
version="1.0.0"
)

class QuestionRequest(BaseModel):


 question: str


@app.get("/")
def home():


 return {
    "message": (
        "Educational Multi-Agent AI API is running."
    )
}


@app.post("/solve")
def solve_question(request: QuestionRequest):
    question = request.question
    monitor = BehaviorMonitor()

    # -----------------------------------
    # PLANNER AGENT
    # -----------------------------------
    learning_plan = run_planner_agent(question)
    monitor.log_event(
        agent="Planner",
        action="Create Learning Plan",
        message=learning_plan
    )

    # -----------------------------------
    # TUTOR AGENT
    # -----------------------------------
    tutor_answer = run_tutor_agent(question, learning_plan)
    monitor.log_event(
        agent="Tutor",
        action="Teach Student",
        message=tutor_answer
    )

    # -----------------------------------
    # EVALUATOR AGENT
    # -----------------------------------
    evaluation = run_evaluator_agent(question, tutor_answer)
    monitor.log_event(
        agent="Evaluator",
        action="Evaluate Answer",
        message=evaluation
    )

    # -----------------------------------
    # FEEDBACK AGENT
    # -----------------------------------
    feedback = run_feedback_agent(tutor_answer, evaluation)
    monitor.log_event(
        agent="Feedback",
        action="Generate Feedback",
        message=feedback
    )

    result = {
        "question": question,
        "learning_plan": learning_plan,
        "tutor_answer": tutor_answer,
        "evaluation": evaluation,
        "feedback": feedback,
        "interaction_logs": monitor.get_logs()
    }

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    result_file = RESULTS_DIR / f"solve_{timestamp}.json"
    result_file.write_text(json.dumps(result, indent=2), encoding="utf-8")

    result["result_file"] = str(result_file.relative_to(BASE_DIR))
    return result

