import os
from dotenv import load_dotenv

load_dotenv()

from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub



def lookup(name: str) -> str:
    return os.getenv("MY_LINKEDIN_PROFILE")


if __name__ == "__main__":
    profile_url = lookup("John Doe")
    print(profile_url)
