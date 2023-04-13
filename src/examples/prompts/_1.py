# TLDR
"""Example of a prompt template"""

from langchain import PromptTemplate

def main():
    template = """
    I want you to act as a naming consultant for new companies.

    Here are some examples of good company names:

    - search engine, Google
    - social media, Facebook
    - video sharing, YouTube

    The name should be short, catchy and easy to remember.

    What is a good name for a company that makes {product}?
    """

    prompt = PromptTemplate(
        input_variables=["product"],
        template=template,
    )

    # print(prompt)
    print('{}'.format(prompt.template))