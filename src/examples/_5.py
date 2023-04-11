# TLDR
"""Using ConversationChain"""

from langchain import OpenAI, ConversationChain


def main():
    llm = OpenAI(temperature=0)
    conversation = ConversationChain(llm=llm, verbose=True)

    conversation.predict(input="Hi there!")