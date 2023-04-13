# TLDR
"""Hugging Face Length Function"""

from transformers import GPT2TokenizerFast
from langchain.text_splitter import CharacterTextSplitter

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

# This is a long document we can split up.
with open('./src/examples/text_splitters/state_of_the_union.txt') as f:
    state_of_the_union = f.read()

def main():
    text_splitter = CharacterTextSplitter.from_huggingface_tokenizer(tokenizer, chunk_size=100, chunk_overlap=0)
    texts = text_splitter.split_text(state_of_the_union)
    
    print(texts[0])