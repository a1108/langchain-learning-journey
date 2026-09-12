from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

response = llm.invoke(
    "What is Python? Explain in one sentence."
)
print("================================")
print(response)
print("================================")
print(type(response).__name__)
print("================================")
print(response.content)
print("================================")
print(response.usage_metadata["total_tokens"])
print("================================")

