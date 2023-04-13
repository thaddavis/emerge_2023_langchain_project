# TLDR
"""LLM Chain"""

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
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

def main():
    chat = ChatOpenAI(temperature=0)

    human_message = HumanMessage(content="Translate this sentence from English to French. I love artificial intelligence.")
    chat_prompt = ChatPromptTemplate.from_messages([human_message])
    chain = LLMChain(llm=chat, prompt=chat_prompt)

    res = chain.run(input_language="English", output_language="French", text="I love programming.")

    # print(res)
    
    chat = ChatOpenAI(streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True, temperature=0)
    resp = chat([HumanMessage(content="Write me a song about sparkling water.")])

    print(resp)