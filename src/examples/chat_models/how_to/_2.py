# TLDR
"""Few Shot Technique Examples"""

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

    template="You are a helpful assistant that translates english to pirate."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    example_human = SystemMessagePromptTemplate.from_template("Hi", additional_kwargs={"name": "example_user"})
    example_ai = SystemMessagePromptTemplate.from_template("Argh me mateys", additional_kwargs={"name": "example_assistant"})
    human_template="{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, example_human, example_ai, human_message_prompt])
    chain = LLMChain(llm=chat, prompt=chat_prompt)
    # get a chat completion from the formatted messages
    resp = chain.run("I love programming.")

    print(resp)