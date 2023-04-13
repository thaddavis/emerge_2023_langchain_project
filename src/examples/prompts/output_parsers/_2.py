# TLDR
"""CommaSeparatedListOutputParser"""

from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI


def main():
    output_parser = CommaSeparatedListOutputParser()

    format_instructions = output_parser.get_format_instructions()
    prompt = PromptTemplate(
        template="List five {subject}.\n{format_instructions}",
        input_variables=["subject"],
        partial_variables={"format_instructions": format_instructions}
    )

    model = OpenAI(temperature=0)

    _input = prompt.format(subject="ice cream flavors")
    output = model(_input)

    res = output_parser.parse(output)
    print(res)