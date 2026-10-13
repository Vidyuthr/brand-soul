from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.messages import HumanMessage
from pydantic import BaseModel

from app.agents.brand_agent import agent as agent_graph

app = FastAPI(title="Brand Soul AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserPromptInput(BaseModel):
    raw_text: str


class AgentResponse(BaseModel):
    message: str


@app.post("/chat")
async def send_user_input_to_llm(body: UserPromptInput) -> AgentResponse:
    agent_state = {
        "messages": [HumanMessage(content=body.raw_text)],
        "brand_soul": {},
        "is_complete": False,
    }

    result = agent_graph.invoke(agent_state)
    return AgentResponse(message=result["messages"][-1].content)


@app.post("/generate-soul")
async def generate_soul(body: UserPromptInput):
    return {"message": "Soul gen starting"}