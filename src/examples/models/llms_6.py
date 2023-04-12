# TLDR
"""InMemoryCache"""

import time
from langchain.llms import OpenAI
import langchain
from langchain.cache import InMemoryCache

def main():
    langchain.llm_cache = InMemoryCache()
    # To make the caching really obvious, lets use a slower model.
    llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2)
    tic = time.perf_counter()
    # The first time, it is not yet in cache, so it should take longer
    llm("Tell me a joke")
    toc = time.perf_counter()
    print(f"{toc - tic:0.4f} seconds")

    tic = time.perf_counter()
    # The first time, it is not yet in cache, so it should take longer
    llm("Tell me a joke")
    toc = time.perf_counter()
    print(f"{toc - tic:0.4f} seconds")
