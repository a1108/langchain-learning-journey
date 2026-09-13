from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI


class Employee(BaseModel):
    name: str = Field(
        description="Employee's name"
    )
    technology: str = Field(
        description="Technology the employee works with"
    )
    experience: int = Field(
        description="Employee's experience in years",
    )

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

structured_prompt = llm.with_structured_output(Employee)

text = input("Enter employee information: ")

employee = structured_prompt.invoke(text)

print("\nEmployee Details:")
print(employee)
print("--------------------------------")

print("Name:", employee.name)
print("Technology:", employee.technology)
print("Experience:", employee.experience)   
