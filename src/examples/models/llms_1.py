# TLDR
"""Getting Started - Generate Text"""

from langchain.llms import OpenAI

def main():
    llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)
    res = llm("Tell me a joke")

    print(res)