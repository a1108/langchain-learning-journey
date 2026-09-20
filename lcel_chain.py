from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

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
    model="gemini-3.6-flash"
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
print(response.text)
print(type(response).__name__)
print(type(chain).__name__)

