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
    # res = chat([HumanMessage(content="Translate this sentence from English to French. I love programming.")])

    messages = [
        SystemMessage(content="You are a helpful assistant that translates English to French."),
        HumanMessage(content="Translate this sentence from English to French. I love programming.")
    ]
    res = chat(messages)

    print('res', res)