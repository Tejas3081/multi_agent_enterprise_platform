
from app.agents.planner_agent import planner_agent
from app.agents.code_agent import code_agent
from app.agents.documentation_agent import documentation_agent

def run_workflow(task):
    plan = planner_agent(task)
    code = code_agent(plan)
    docs = documentation_agent(code)

    return {
        "plan": plan,
        "generated_code": code,
        "documentation": docs
    }
