from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage
from app.agents.brand_agent import agent

result = agent.invoke({
    "messages": [HumanMessage(content="I run a coffee shop")],
    "brand_soul": {},
    "is_complete": False,
})