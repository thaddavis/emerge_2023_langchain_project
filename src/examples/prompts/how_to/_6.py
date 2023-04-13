# TLDR
"""Load Prompt Template from .json, .yaml, and subreferenced files"""

from langchain.prompts import load_prompt

def main():

    prompt = load_prompt("./src/examples/prompts/how_to/few_shot_prompt.yaml")
    print(prompt.format(adjective="funny"))
