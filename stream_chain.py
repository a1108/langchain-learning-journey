from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Create Prompt
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

# Create Model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

# Create Parser
parser = StrOutputParser()

# Create Chain
chain = prompt_template | llm | parser

# Get user input
topic = input('Enter your topic name: ')

# Stream the response
for chunk in chain.stream({"topic": topic}):	
	print(chunk, end="", flush=True)

print()


