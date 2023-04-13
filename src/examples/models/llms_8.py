# TLDR
"""Streaming LLM output with various LLM classes"""

from langchain.llms import OpenAI, Anthropic
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.schema import HumanMessage

def main():
    # with OpenAI LLM
    # llm = OpenAI(streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True, temperature=0)
    # resp = llm("Write me a song about sparkling water.")
    # llm.generate(["Tell me a joke."])

    # with ChatOpenAI LLM
    chat = ChatOpenAI(streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True, temperature=0)
    resp = chat([HumanMessage(content="Write me a song about sparkling water.")])
    
    # with Anthropic LLM
    llm = Anthropic(streaming=True, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), verbose=True, temperature=0)
    llm("Write me a song about sparkling water.")