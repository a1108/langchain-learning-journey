from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt_template = PromptTemplate.from_template(
    """
    Explain {topic} in simple English
    in about 5 short points.
    """,
    partial_variables=
        {
            
            "topic": "Python"
        }
)


llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

parser = StrOutputParser()

chain = prompt_template | llm | parser

inputs = [
    {"topic": "Python"}, 
    {"topic": "Java"},
    {"topic": "SQL"}
]

response = chain.batch(inputs)

for result in response:	
	print(result)
	print("-----------------------------------------------")

print()
print(type(response).__name__) #list
print(type(chain).__name__)

