
# from app.agents.groq_client import ask_groq

# def planner_agent(task):
#     prompt = f"Create an execution plan for: {task}"
#     return ask_groq(prompt)

from app.agents.groq_client import ask_groq

async def planner_agent(state):

    task = state["task"]

    prompt = f"""
    Create execution plan for:

    {task}
    """

    result = await ask_groq(prompt)

    state["plan"] = result

    return state