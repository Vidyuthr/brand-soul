from langchain_core.messages import HumanMessage
from app.agents.brand_agent import agent
from dotenv import load_dotenv

load_dotenv()



result = agent.invoke({
    "messages": [HumanMessage(content="I run a coffee shop")],
    "brand_soul": {},
    "is_complete": False,
})