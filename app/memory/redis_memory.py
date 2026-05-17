from app.agents.groq_client import ask_groq

async def qa_agent(state):

    code = state["generated_code"]

    prompt = f"""
    Review this code.

    Find:
    - bugs
    - vulnerabilities
    - performance issues

    Code:
    {code}
    """

    result = await ask_groq(prompt)

    state["qa_report"] = result

    return state