
# from fastapi import FastAPI
# from app.agents.orchestrator import run_workflow

# app = FastAPI(title="Multi Agent Enterprise Platform")

# @app.get("/")
# def home():
#     return {"message": "AI Multi-Agent Platform Running"}

# @app.post("/execute")
# def execute(task: str):
#     result = run_workflow(task)
#     return {"result": result}


from fastapi import FastAPI
from app.api.routes import router
from app.websocket.socket_manager import socket_router

app = FastAPI(title="Enterprise Multi-Agent Platform")

app.include_router(router)
app.include_router(socket_router)

@app.get("/")
async def home():
    return {
        "status": "running"
    }