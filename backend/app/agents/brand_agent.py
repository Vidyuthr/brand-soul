from typing import TypedDict, List, Annotated
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from app.agents.prompts import SYSTEM_PROMPT
import json

# 1. Define the State (The "Memory" of the agent)
class AgentState(TypedDict):
    messages: List[BaseMessage]
    brand_soul: dict
    is_complete: bool

# 2. Initialize the LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)


def call_model(state: AgentState):
    messages = [AIMessage(content=SYSTEM_PROMPT)] + state["messages"]
    response = llm.invoke(messages)
    return response