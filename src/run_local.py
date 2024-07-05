from langchain import PromptTemplate
from langchain import LLMChain
from langchain.llms import ctransformers

B_INST,E_INST ="[INST]","[/INST]"
B_SYS,E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"