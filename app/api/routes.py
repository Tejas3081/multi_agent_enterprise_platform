from fastapi import APIRouter
from app.workflows.graph import app_graph

router = APIRouter()

@router.post("/execute")
async def execute(task: str):

    result = await app_graph.ainvoke({
        "task": task
    })

    return result