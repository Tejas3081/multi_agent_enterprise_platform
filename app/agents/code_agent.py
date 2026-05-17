from app.agents.groq_client import ask_groq


async def code_agent(state):

    plan = state["plan"]

    prompt = f"""
    Generate production-grade Python code.

    Plan:
    {plan}
    """

    result = await ask_groq(prompt)

    state["generated_code"] = result

    return state