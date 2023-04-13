# TLDR
"""Walkthrough of what happens under the hood with Vectorstore indexers"""

from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def main():
    loader = TextLoader('./src/examples/indexers/getting_started/state_of_the_union.txt')
    index = VectorstoreIndexCreator().from_loaders([loader])

    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    db = Chroma.from_documents(texts, embeddings)

    retriever = db.as_retriever()

    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever)

    query = "What did the president say about Ketanji Brown Jackson"
    res = qa.run(query)

    print('res', res)