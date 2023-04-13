# TLDR
"""Tracking Token Usage"""

from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

def main():
    # llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2)

    # with get_openai_callback() as cb:
    #     result = llm("Tell me a joke")
    #     print(f"Total Tokens: {cb.total_tokens}")
    #     print(f"Prompt Tokens: {cb.prompt_tokens}")
    #     print(f"Completion Tokens: {cb.completion_tokens}")
    #     print(f"Successful Requests: {cb.successful_requests}")
    #     print(f"Total Cost (USD): ${cb.total_cost}")

    # with get_openai_callback() as cb:
    #     result = llm("Tell me a joke")
    #     result2 = llm("Tell me a joke")
    #     print(cb.total_tokens)

    llm = OpenAI(temperature=0)
    tools = load_tools(["serpapi", "llm-math"], llm=llm)
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    with get_openai_callback() as cb:
        response = agent.run("Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?")
        print(f"Total Tokens: {cb.total_tokens}")
        print(f"Prompt Tokens: {cb.prompt_tokens}")
        print(f"Completion Tokens: {cb.completion_tokens}")
        print(f"Total Cost (USD): ${cb.total_cost}")