# TLDR
"""Load Prompt Template from .json, .yaml, and subreferenced files"""

from langchain.prompts import load_prompt

def main():
    # Load Prompt Ex. 1
    # prompt = load_prompt("./src/examples/prompts/how_to/simple_prompt.yaml")
    # print(prompt.format(adjective="funny", content="chickens"))

    # Load Prompt Ex. 2
    # prompt = load_prompt("./src/examples/prompts/how_to/simple_prompt.json")
    # print(prompt.format(adjective="funny", content="chickens"))

    # Load Prompt Ex. 3
    prompt = load_prompt("./src/examples/prompts/how_to/simple_prompt_with_template_file.json")
    print(prompt.format(adjective="funny", content="chickens"))