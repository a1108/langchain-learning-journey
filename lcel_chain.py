from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable

load_dotenv()


topic = input('Enter Topic:')
language = input('Enter Language:')
level = input('Enter Level:')

prompt_template = PromptTemplate.from_template(
    """
    Explain {topic} in {language} at {level} level.
    """,
    partial_variables=
    {
        "level": "beginner",
        "topic": "Python",
        "language": "English"
    }
)


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    thinking_budget=0  # Disables thinking tokens, dropping response time to 1-3 seconds
)

chain = prompt_template | llm 

response = chain.invoke(
    {
        "topic": topic,
        "level": level,
        "language": language
    }
)

print()
print(response.content)
print(type(response).__name__)
print(type(chain).__name__)
print("==============================")
print(type(llm))
print(isinstance(llm, Runnable))
