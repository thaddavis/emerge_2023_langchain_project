# TLDR
"""Using a LLMChain to chain together multiple prompts and llms"""

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

def main():
    llm = OpenAI(temperature=0.2)
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    print(chain.run("colorful socks"))