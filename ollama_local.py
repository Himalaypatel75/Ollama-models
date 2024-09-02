from langchain_core.prompts import ChatPromptTemplate
from langchain.llms import Ollama

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = Ollama(base_url="http://localhost:11434", model = "mario")

chain = prompt | model

chain.invoke({"question": "What is LangChain?"})
