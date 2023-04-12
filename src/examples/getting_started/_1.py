# TLDR
"""Sending arbitrary input to ChatGPT"""

from langchain.llms import OpenAI

def main():
    llm = OpenAI(temperature=0.9)
    text = "What would be a good company name for a company that makes colorful socks?"
    print(llm(text))