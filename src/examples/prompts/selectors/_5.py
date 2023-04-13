# TLDR
"""Similarity ExampleSelector"""

from langchain import OpenAI
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

def main():

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

    example_selector = SemanticSimilarityExampleSelector.from_examples(
        # This is the list of examples available to select from.
        examples, 
        # This is the embedding class used to produce embeddings which are used to measure semantic similarity.
        OpenAIEmbeddings(), 
        # This is the VectorStore class that is used to store the embeddings and do a similarity search over.
        Chroma, 
        # This is the number of examples to produce.
        k=1
    )
    similar_prompt = FewShotPromptTemplate(
        # We provide an ExampleSelector instead of examples.
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix="Give the antonym of every input",
        suffix="Input: {adjective}\nOutput:", 
        input_variables=["adjective"],
    )

    llm = OpenAI(model_name="text-ada-001", n=2, best_of=2)
    res = llm(similar_prompt.format(adjective="worried"))

    print(res)