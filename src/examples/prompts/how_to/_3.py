# TLDR
"""Partial Prompt Templates"""

from langchain.prompts import PromptTemplate

def main():
    prompt = PromptTemplate(template="{foo}{bar}", input_variables=["foo", "bar"])
    partial_prompt = prompt.partial(foo="foo")
    print(partial_prompt.format(bar="baz"))

    print()

    prompt = PromptTemplate(template="{foo}{bar}", input_variables=["bar"], partial_variables={"foo": "foo"})
    print(prompt.format(bar="baz"))
