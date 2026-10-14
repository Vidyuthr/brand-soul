# brand_agent.py

from typing import Annotated, List, TypedDict

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver


from app.agents.prompts import SYSTEM_PROMPT

load_dotenv()  # loads .env before the LLM is created


# 1. Define the State (The "Memory" of the agent)
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    brand_soul: dict
    is_complete: bool


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)


# Just invoking LLM response
def call_model(state: AgentState):
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]
    response = llm.invoke(messages)
    print("len of convo ", len(result["messages"]))
    return {"messages": [response]}
    

checkpointer = InMemorySaver()

# Setting up the agentic graph
graph = StateGraph(AgentState)
graph.add_node(call_model)
graph.add_edge(START, "call_model")
graph.add_edge("call_model", END)
agent = graph.compile(checkpointer=checkpointer)