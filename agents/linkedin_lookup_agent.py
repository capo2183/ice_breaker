import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain import hub


def lookup(name: str) -> str:
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini"
    )
     