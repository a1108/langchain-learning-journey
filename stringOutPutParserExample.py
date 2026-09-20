from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

llm_response = llm.invoke(
    "What is Python? Explain in one sentence."
)

parser = StrOutputParser()
parser_response = parser.invoke(llm_response)



print("==============parser_response==================")
print(parser_response)
print("============parser_response type====================")
print(type(parser_response).__name__)

print("==============llm_response==================")
print(llm_response)
print("============llm_response type====================")
print(type(llm_response).__name__)