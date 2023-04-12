# TLDR
"""Intro to some of the properties and methods of a Base LLM class"""

from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any

class CustomLLM(LLM):
    
    n: int
        
    @property
    def _llm_type(self) -> str:
        return "custom"
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        return prompt[:self.n]
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"n": self.n}
    
def main():
    llm = CustomLLM(n=10)
    llm("This is a foobar thing")
    print(llm)