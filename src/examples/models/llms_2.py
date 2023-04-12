# TLDR
"""Getting Started - Multiple Text Generations"""

from langchain.llms import OpenAI

def main():
    llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)
    llm_result = llm.generate(["Tell me a joke", "Tell me a poem"]*15)
    len(llm_result.generations)
    res = llm_result.generations[0]
    # print(res)
    res = llm_result.generations[-1]
    # print(res)

    # for r in res:
    #     print('___')
    #     print(r.text)

    print(llm_result.llm_output)

