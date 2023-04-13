# TLDR
"""Configure LLM from .json file"""

from langchain.llms import OpenAI
from langchain.llms.loading import load_llm

# import json
# f = open('./src/examples/models/llms_7.json')
# data = json.load(f)

def main():
    llm = load_llm("./src/examples/models/llms_7.json")
    res = llm("Tell me a joke")
    print(res)