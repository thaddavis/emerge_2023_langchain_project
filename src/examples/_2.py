# TLDR
"""Using a PromptTemplate then generating a prompt"""

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

def main():
    llm = OpenAI(temperature=0.9)
    prompt_tmplt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    prompt = prompt_tmplt.format(product="colorful socks")
    print(prompt)
    print(llm(prompt))