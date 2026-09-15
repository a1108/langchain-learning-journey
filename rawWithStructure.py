from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI


class Employee(BaseModel):
    name: str = Field(
        description="Employee's name"
    )
    technology: str | None = Field(
        default=None,
        description="Technology the employee works with"
    )
    experience: int | None = Field(
        default=None,
        description="Employee's experience in years",
    )

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

structured_prompt = llm.with_structured_output(Employee,include_raw=True)

text = input("Enter employee information: ")

prompt = f"""
Extract employee information.

Rules:
1. Use only the supplied text.
2. Do not invent information.
3. If optional information is unavailable, use null.

Text:
{text}"""

result = structured_prompt.invoke(prompt)


print("\n---------- RAW ----------")
print(result["raw"])

print("\n---------- PARSED ----------")
print(result["parsed"])

print("\n---------- PARSING ERROR ----------")
print(result["parsing_error"])


