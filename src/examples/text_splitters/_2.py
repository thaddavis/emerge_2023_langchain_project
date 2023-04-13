from langchain.text_splitter import CharacterTextSplitter

# This is a long document we can split up.
with open('./src/examples/text_splitters/state_of_the_union.txt') as f:
    state_of_the_union = f.read()

def main():
    text_splitter = CharacterTextSplitter(
        separator = "\n\n",
        chunk_size = 1000,
        chunk_overlap  = 200,
        length_function = len,
    )

    texts = text_splitter.create_documents([state_of_the_union])
    print(texts[0])

    print()

    metadatas = [{"document": 1}, {"document": 2}]
    documents = text_splitter.create_documents([state_of_the_union, state_of_the_union], metadatas=metadatas)
    print(documents[0])