from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)


question = HumanMessage(
    content="""
    What is my name?

    If my name is not available in the
    supplied conversation, say "I don't know".
    """
)


# WITHOUT HISTORY

response1 = llm.invoke(
    [question]
)

print("WITHOUT HISTORY")
print("----------------")
print(response1.text)


# WITH HISTORY

messages = [
    HumanMessage(
        content="My name is Ankit."
    ),

    AIMessage(
        content="Nice to meet you."
    ),

    question
]

response2 = llm.invoke(
    messages
)

print("\nWITH HISTORY")
print("------------")
print(response2.text)
