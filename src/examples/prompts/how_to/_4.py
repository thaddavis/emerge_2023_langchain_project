# TLDR
"""Initializing Partial Prompt Templates w/ Dynamic Values"""

from langchain.prompts import PromptTemplate
from datetime import datetime

def _get_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")

def main():
    prompt = PromptTemplate(
        template="Tell me a {adjective} joke about the day {date}", 
        input_variables=["adjective", "date"]
    )
    partial_prompt = prompt.partial(date=_get_datetime)
    print(partial_prompt.format(adjective="funny"))

    print()

    prompt = PromptTemplate(
        template="Tell me a {adjective} joke about the day {date}", 
        input_variables=["adjective"],
        partial_variables={"date": _get_datetime}
    )
    print(prompt.format(adjective="funny"))

