# TLDR
"""Markdown Text Splitter"""

from langchain.text_splitter import MarkdownTextSplitter

def main():
    markdown_text = """
    # 🦜️🔗 LangChain

    ⚡ Building applications with LLMs through composability ⚡

    ## Quick Install

    ```bash
    # Hopefully this code block isn't split
    pip install langchain
    ```

    As an open source project in a rapidly developing field, we are extremely open to contributions.
    """
    markdown_splitter = MarkdownTextSplitter(chunk_size=100, chunk_overlap=0)

    docs = markdown_splitter.create_documents([markdown_text])

    print(docs)