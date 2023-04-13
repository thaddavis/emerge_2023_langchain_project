# TLDR
"""Maximal Marginal Relevance ExampleSelector"""

"""
Issues ran into were:

- had to install faiss: `poetry add faiss-cpu`
"""

from langchain import OpenAI
from langchain.prompts.example_selector import MaxMarginalRelevanceExampleSelector
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Input: {input}\nOutput: {output}",
)

# These are a lot of examples of a pretend task of creating antonyms.
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
    {"input": "energetic", "output": "lethargic"},
    {"input": "sunny", "output": "gloomy"},
    {"input": "windy", "output": "calm"},
]

def main():
    example_selector = MaxMarginalRelevanceExampleSelector.from_examples(
        # This is the list of examples available to select from.
        examples, 
        # This is the embedding class used to produce embeddings which are used to measure semantic similarity.
        OpenAIEmbeddings(), 
        # This is the VectorStore class that is used to store the embeddings and do a similarity search over.
        FAISS, 
        # This is the number of examples to produce.
        k=2
    )
    
    mmr_prompt = FewShotPromptTemplate(
        # We provide an ExampleSelector instead of examples.
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix="Give the antonym of every input",
        suffix="Input: {adjective}\nOutput:", 
        input_variables=["adjective"],
    )

    # Input is a feeling, so should select the happy/sad example as the first one
    print(mmr_prompt.format(adjective="worried"))

    print()

    # Let's compare this to what we would just get if we went solely off of similarity
    similar_prompt = FewShotPromptTemplate(
        # We provide an ExampleSelector instead of examples.
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix="Give the antonym of every input",
        suffix="Input: {adjective}\nOutput:", 
        input_variables=["adjective"],
    )
    similar_prompt.example_selector.k = 2
    print(similar_prompt.format(adjective="worried"))

    llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)
    res = llm(similar_prompt.format(adjective="worried"))

    print(res)