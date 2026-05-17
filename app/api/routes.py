# from fastapi import APIRouter
# from app.workflows.graph import app_graph

# router = APIRouter()

# @router.post("/execute")
# async def execute(task: str):

#     result = await app_graph.ainvoke({
#         "task": task
#     })

#     return result

from fastapi import APIRouter
from app.workflows.graph import app_graph
from app.database.mongo import workflow_collection

router = APIRouter()

@router.post("/execute")
async def execute(task: str):

    result = await app_graph.ainvoke({
        "task": task
    })

    workflow_collection.insert_one({
        "task": task,
        "result": result
    })

    return result

@router.get("/history")
async def history():

    data = list(
        workflow_collection.find(
            {},
            {"_id": 0}
        )
    )

    return data