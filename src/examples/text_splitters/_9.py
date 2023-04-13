# TLDR
"""SpacyTextSplitter"""

"""Issues ran into: needed to install space"""

from langchain.text_splitter import SpacyTextSplitter

# This is a long document we can split up.
with open('./src/examples/text_splitters/state_of_the_union.txt') as f:
    state_of_the_union = f.read()

def main():

    text_splitter = SpacyTextSplitter(chunk_size=1000)
    texts = text_splitter.split_text(state_of_the_union)
    print(texts[0])