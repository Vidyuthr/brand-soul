import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
load_dotenv()

from app.agents.brand_agent import app as agent_graph
import json

app = FastAPI(title='Brand Soul AI API')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def send_user_input_to_llm(user_input: str):
    agent_state = {
        "messages": [HumanMessage(content=user_input)],
        "brand_soul": {},
        "is_complete": False
    }

    result = agent_graph.call_model(agent_state)
    return result

@app.post("/generate-soul")
async def generate_soul(user_input: str):
    return {"message": "Soul gen starting"}
