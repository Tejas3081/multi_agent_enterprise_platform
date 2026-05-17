from fastapi import APIRouter, WebSocket
from app.agents.planner_agent import planner_agent
from app.agents.code_agent import code_agent
from app.agents.documentation_agent import documentation_agent
from app.agents.qa_agent import qa_agent

socket_router = APIRouter()


@socket_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    print("Client Connected")

    while True:

        task = await websocket.receive_text()

        state = {
            "task": task
        }

        # Planner Agent
        await websocket.send_text(
            "Planner Agent Thinking..."
        )

        state = await planner_agent(state)

        await websocket.send_text(
            state["plan"]
        )

        # Code Agent
        await websocket.send_text(
            "Code Agent Generating..."
        )

        state = await code_agent(state)

        await websocket.send_text(
            state["generated_code"]
        )

        # Documentation Agent
        await websocket.send_text(
            "Documentation Agent Writing..."
        )

        state = await documentation_agent(state)

        await websocket.send_text(
            state["documentation"]
        )

        # QA Agent
        await websocket.send_text(
            "QA Agent Reviewing..."
        )

        state = await qa_agent(state)

        await websocket.send_text(
            state["qa_report"]
        )

        await websocket.send_text(
            "Workflow Completed Successfully!"
        )