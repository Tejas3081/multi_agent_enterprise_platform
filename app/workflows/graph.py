from langgraph.graph import StateGraph

from app.agents.planner_agent import planner_agent
from app.agents.code_agent import code_agent
from app.agents.documentation_agent import documentation_agent
from app.agents.qa_agent import qa_agent

workflow = StateGraph(dict)

workflow.add_node("planner", planner_agent)
workflow.add_node("coder", code_agent)
workflow.add_node("documentation", documentation_agent)
workflow.add_node("qa", qa_agent)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "coder")
workflow.add_edge("coder", "documentation")
workflow.add_edge("documentation", "qa")

app_graph = workflow.compile()