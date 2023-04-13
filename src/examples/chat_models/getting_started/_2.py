# TLDR
"""Batch Messages With Chat Models"""

from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

def main():
    chat = ChatOpenAI(temperature=0)

    batch_messages = [
        [
            SystemMessage(content="You are a helpful assistant that translates English to French."),
            HumanMessage(content="Translate this sentence from English to French. I love programming.")
        ],
        [
            SystemMessage(content="You are a helpful assistant that translates English to French."),
            HumanMessage(content="Translate this sentence from English to French. I love artificial intelligence.")
        ],
    ]
    result = chat.generate(batch_messages)
    # print(result)

    for r in result:
        print("--- ---")
        print(r)

    print(result.llm_output)