# TLDR
"""Chat Models"""

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import json

def main():
    chat = ChatOpenAI(temperature=0)
    
    """Single Messages"""
    # res= chat([HumanMessage(content="Translate this sentence from English to French. I love programming.")])
    # print('Single Messages response', res)
    # # -> AIMessage(content="J'aime programmer.", additional_kwargs={})

    """Multiple Messages"""
    # messages = [
    #     SystemMessage(content="You are a helpful assistant that translates English to French."),
    #     HumanMessage(content="Translate this sentence from English to French. I love programming.")
    # ]
    # res = chat(messages)
    # print('Multiple Messages response', res)
    # # -> AIMessage(content="J'aime programmer.", additional_kwargs={})

    """Batch Messages"""
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
    res = chat.generate(batch_messages)
    print(res)
    for r in res.generations:
        print(r)
    print(res.llm_output['token_usage'])
    