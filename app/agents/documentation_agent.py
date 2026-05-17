
from app.agents.groq_client import ask_groq

async def documentation_agent(state):

    code = state["generated_code"]

    prompt = f"""
    Generate developer documentation for this code:


    Code:
    {code}
    """

    result = await ask_groq(prompt)

    state["documentation"] = result

    return state