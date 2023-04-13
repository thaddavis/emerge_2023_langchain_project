# TLDR
"""Chat Prompt Template"""

from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
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
    template="You are a helpful assistant that translates {input_language} to {output_language}."
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template="{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    # get a chat completion from the formatted messages
    res = chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_messages()
    
    print('res', res)
    print()

    prompt=PromptTemplate(
        template="You are a helpful assistant that translates {input_language} to {output_language}.",
        input_variables=["input_language", "output_language"],
    )
    system_message_prompt = SystemMessagePromptTemplate(prompt=prompt)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt])

    res = chat_prompt.format_prompt(input_language="English", output_language="French", text="I love programming.").to_messages()
    print('res', res)
    print()