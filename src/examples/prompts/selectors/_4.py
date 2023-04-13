# TLDR
"""NGram Overlap ExampleSelector"""

from langchain.prompts import PromptTemplate
from langchain.prompts.example_selector.ngram_overlap import NGramOverlapExampleSelector
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
    example_prompt = PromptTemplate(
        input_variables=["input", "output"],
        template="Input: {input}\nOutput: {output}",
    )
    example_selector = NGramOverlapExampleSelector(
        # These are the examples it has available to choose from.
        examples=examples, 
        # This is the PromptTemplate being used to format the examples.
        example_prompt=example_prompt, 
        # This is the threshold, at which selector stops.
        # It is set to -1.0 by default.
        threshold=-1.0,
        # For negative threshold:
        # Selector sorts examples by ngram overlap score, and excludes none.
        # For threshold greater than 1.0:
        # Selector excludes all examples, and returns an empty list.
        # For threshold equal to 0.0:
        # Selector sorts examples by ngram overlap score,
        # and excludes those with no ngram overlap with input.
    )
    dynamic_prompt = FewShotPromptTemplate(
        # We provide an ExampleSelector instead of examples.
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix="Give the Spanish translation of every input",
        suffix="Input: {sentence}\nOutput:", 
        input_variables=["sentence"],
    )

    # An example input with large ngram overlap with "Spot can run."
    # and no overlap with "My dog barks."
    print(dynamic_prompt.format(sentence="Spot can run fast."))

    print('--- --- --- --- ---')

    # You can add examples to NGramOverlapExampleSelector as well.
    new_example = {"input": "Spot plays fetch.", "output": "Spot juega a buscar."}

    example_selector.add_example(new_example)
    print(dynamic_prompt.format(sentence="Spot can run fast."))

    print('--- --- --- --- ---')

    example_selector.threshold=0.0
    print(dynamic_prompt.format(sentence="Spot can run fast."))

    print('--- --- --- --- ---')

    example_selector.threshold=0.09
    print(dynamic_prompt.format(sentence="Spot can play fetch."))

    print('--- --- --- --- ---')

    example_selector.threshold=1.0+1e-9
    print(dynamic_prompt.format(sentence="Spot can play fetch."))