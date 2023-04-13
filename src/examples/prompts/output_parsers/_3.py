# TLDR
"""OutputFixingParser"""

from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.output_parsers import OutputFixingParser
from pydantic import BaseModel, Field, validator
from typing import List

class Actor(BaseModel):
    name: str = Field(description="name of an actor")
    film_names: List[str] = Field(description="list of names of films they starred in")

def main():
    actor_query = "Generate the filmography for a random actor."
    parser = PydanticOutputParser(pydantic_object=Actor)
    misformatted = "{'name': 'Tom Hanks', 'film_names': ['Forrest Gump']}"
    # parser.parse(misformatted)

    new_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI())
    res = new_parser.parse(misformatted)
    print(res)