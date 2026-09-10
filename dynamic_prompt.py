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

  
  Use:
    - 5 important points
    - One real-life example
    """,
    partial_variables=
    {
        "level": "beginner",
        "topic": "Python",
        "language": "English"
    }
)

prompt_value = prompt_template.invoke(
    {
        "topic": topic,
        "level": level,
        "language": language
    }
)

print(prompt_value.to_string()) #generated final prompt
print()
print()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)



response = llm.invoke(prompt_value)

print()
print(response.content)
print(type(response).__name__)

