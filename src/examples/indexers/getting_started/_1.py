# TLDR
"""Getting started with Vectorstore indexers"""

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

def main():
    
    loader = TextLoader('./src/examples/indexers/getting_started/state_of_the_union.txt')
    index = VectorstoreIndexCreator().from_loaders([loader])
    
    query = "What did the president say about Ketanji Brown Jackson"
    res = index.query(query)

    print('res', res)

    query = "What did the president say about Ketanji Brown Jackson"
    res = index.query_with_sources(query)

    print('res', res)