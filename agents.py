import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import SecretStr

# Force load .env from the same folder as this file
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError(
        "\n\n❌ GROQ_API_KEY not found!\n"
        "Create a .env file in the research-mind folder with:\n"
        "GROQ_API_KEY=your_key_here\n"
        "Get a free key at https://console.groq.com\n"
    )

# FREE model via Groq
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=(SecretStr(api_key)),
)

def build_search_agent():
    return create_react_agent(model=llm, tools=[web_search])

def build_reader_agent():
    return create_react_agent(model=llm, tools=[scrape_url])

writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()

critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()
