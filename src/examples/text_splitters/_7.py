# TLDR
"""Python Code Text Splitter"""

from langchain.text_splitter import PythonCodeTextSplitter

def main():
    python_text = """
    class Foo:

        def bar():
    
    
        def foo():

        def testing_func():

        def bar():
    """
    python_splitter = PythonCodeTextSplitter(chunk_size=30, chunk_overlap=0)

    docs = python_splitter.create_documents([python_text])

    print(docs)