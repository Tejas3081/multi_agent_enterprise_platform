from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017/"
)

db = client["agentic_ai"]

workflow_collection = db["workflows"]