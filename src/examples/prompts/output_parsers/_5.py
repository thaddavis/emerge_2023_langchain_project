# TLDR
"""RetryOutputParser"""

from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser, OutputFixingParser, RetryOutputParser, RetryWithErrorOutputParser
from pydantic import BaseModel, Field, validator
from typing import List

class Action(BaseModel):
        action: str = Field(description="action to take")
        action_input: str = Field(description="input to the action")

def main():
    template = """Based on the user question, provide an Action and Action Input for what step should be taken.
    {format_instructions}
    Question: {query}
    Response:"""
    
    parser = PydanticOutputParser(pydantic_object=Action)

    prompt = PromptTemplate(
        template="Answer the user query.\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()} 
    )

    prompt_value = prompt.format_prompt(query="who is leo di caprios gf?")
    bad_response = '{"action": "search"}'

    # fix_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI())
    # fix_parser.parse(bad_response)
    
    # --- --- --- --- ---

    retry_parser = RetryWithErrorOutputParser.from_llm(parser=parser, llm=OpenAI(temperature=0))

    print('___ ___ ___')

    res = retry_parser.parse_with_prompt(bad_response, prompt_value)
    print('res', res)