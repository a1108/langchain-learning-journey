# LangChain Learning Journey

This repository documents my hands-on AI learning journey using Python, LangChain, Google Gemini, and Pydantic.

I am learning to build AI applications step by step: starting with basic prompts, moving to dynamic prompts, and creating practical mini-projects. My next learning phase will focus on LangGraph workflows and AI agents.

## What I Am Learning

- Python virtual environments
- Environment variables and API-key security
- Google Gemini integration with LangChain
- Static prompts
- Dynamic prompts with user input
- Prompt templates
- LangChain Expression Language (LCEL) and chaining with the `|` operator
- Output parsers: string output and structured output
- System and human messages
- Building practical AI applications
- Pydantic models and data validation

## Projects

### 1. Static Prompt

File: `static_prompt.py`

This example sends a fixed question to Gemini and prints the AI response.

Concepts practiced:

- Loading variables from `.env`
- Creating a `ChatGoogleGenerativeAI` model
- Calling a model with `.invoke()`
- Printing the response text
- Understanding the `AIMessage` response type
- Reading token usage with `response.usage_metadata`

### 2. Dynamic Prompt

File: `dynamic_prompt.py`

This example asks the user for a topic, language, and learning level. It uses LangChain's `PromptTemplate` to create a customized AI prompt.

Example input:

```text
Enter Topic: SQL
Enter Language: Hindi
Enter Level: advanced
```

### 3. AI Travel Guide

File: `travel_guide.py`

This mini-project creates a personalized travel plan based on user input.

The user provides:

- Destination
- Number of days
- Budget
- Main interest

The AI generates:

- Places to visit
- A daily travel schedule
- Food suggestions
- Practical travel tips

Example input:

```text
Enter destination: Goa
Enter number of days: 5
Enter budget: High
Enter main interest: Fishing
```

### 4. School Data Validation with Pydantic

File: `pydantic_school.py`

This example uses Pydantic models to validate student, teacher, and school data.

Concepts practiced:

- Creating models with `BaseModel`
- Validating strings and integers with `Field`
- Using `ge`, `le`, and `gt` validation rules
- Creating optional fields with `str | None` and `default=None`
- Using default values, such as a default school ID
- Creating nested models with `list[Student]` and `list[Teacher]`
- Handling invalid input with `ValidationError`
- Converting a model to a dictionary with `.model_dump()`

Example:

```text
Student:
first_name='Ankit' middle_name='Kumar' last_name='Gupta' age=20 grade='A'

School as dictionary:
{'name': 'DurgaClasses', 'school_id': 101, 'students': [{'first_name': 'Ankit', 'middle_name': 'Kumar', 'last_name': 'Gupta', 'age': 20, 'grade': 'A'}, {'first_name': 'Sumit', 'middle_name': None, 'last_name': None, 'age': 18, 'grade': 'A+'}], 'teachers': [{'name': 'Durga', 'age': 30, 'subject': 'Programming'}, {'name': 'Rahul', 'age': 42, 'subject': 'Science'}]}

School with default ID:
100

Class names:
School
Student
Teacher

== Validation Error Scenario ==
1 validation error for Student
age
  Input should be greater than or equal to 5 [type=greater_than_equal, input_value=4, input_type=int]
```


### 5. Candidate Profile Extraction (Structured Output)

File: candidate_extraction.py

This project parses and scrapes unstructured text from user inputs to extract validated applicant details using Pydantic and Gemini.

Concepts practiced:

- Enforcing JSON schema generation using .with_structured_output()
- Parsing raw text directly into structured Pydantic model instances
- Validating extracted employee attributes (name, technology, years of experience)

Example:

```text
Enter employee information: Ankit began his career at Ericsson, joining as a Java Developer on September 15, 2015.


Employee Details:
name='Ankit' 
technology='Java'
experience=11

```
### 6. Raw and Structured Output Handling

File: `rawWithStructure.py`

This example demonstrates how to capture and inspect both the raw model output and the validated Pydantic object using the `include_raw=True` option.

Concepts practiced:

- Enabling `include_raw=True` in `.with_structured_output()`
- Accessing raw model output (`result["raw"]`), parsed Pydantic objects (`result["parsed"]`), and runtime parsing errors (`result
  ["parsing_error"]`)
- Managing optional fields (`str | None`, `int | None`) with default values of `None` to eliminate model hallucinations
- Comparing native JSON `null` serialization against Python `None` values

Example:

```text
Enter employee information: i am ankit and i am also java backend developer

---------- RAW ----------
content=[{'type': 'text', 'text': '{"name":"ankit","technology":"java backend developer","experience":"null"}', ...}]

---------- PARSED ----------
name='ankit' technology='java backend developer' experience=None

---------- PARSING ERROR ----------
None
```

### 7. Support Ticket Classification with Literal Constraints

File: `supportTicketWithLiteral.py`

This project classifies and structures unstructured customer support requests into categorized, prioritized support tickets using Pydantic `Literal` types and Gemini.

Concepts practiced:

- Restricting model categorical outputs using Python's `typing.Literal`
- Applying range validation (`ge`, `le`) to numerical scoring fields
- Generating concise summaries while performing multi-label classification
- Building automated triage pipelines with `.with_structured_output()`

Example:

```text
Enter customer issue: I forgot my password and cannot login to my account.

SUPPORT TICKET
------------------
Category : account
Priority : medium
Severity : 3
Summary  : User forgot password and cannot log into account
```

### 8. LangChain Expression Language (LCEL) Chain

File: `langChainExpressionLanguage.py`

This example asks the user for a topic, language, and learning level, then builds a chain using LangChain Expression Language (LCEL). A `PromptTemplate` with default values is piped into Gemini with the `|` operator, and the whole chain is run with a single `.invoke()` call.

Concepts practiced:

- Composing components with the LCEL `|` operator (`prompt_template | llm`)
- Setting default values with `partial_variables` (topic: Python, language: English, level: beginner)
- Overriding those defaults by passing values to `chain.invoke()`
- Running a chain with a dictionary of inputs
- Comparing the response type (`AIMessage`) with the chain type (`RunnableSequence`)

Example input:

```text
Enter Topic: SQL
Enter Language: Hindi
Enter Level: advanced
```

The script also prints the type names at the end:

```text
AIMessage
RunnableSequence
```

### 9. String Output Parser

File: `str_output_parser.py`

This example calls Gemini with a fixed question, then passes the model response through `StrOutputParser` to compare the raw `AIMessage` with the parsed plain string.

Concepts practiced:

- Creating a parser with `StrOutputParser()`
- Running a parser on its own with `parser.invoke(llm_response)`, without building a chain
- Converting an `AIMessage` into a plain Python `str`
- Comparing the raw model response with the parsed response
- Confirming the types with `type(...).__name__`

Example output:

```text
==============parser_response==================
Python is ...
============parser_response type====================
str
==============llm_response==================
content=[{'type': 'text', 'text': 'Python is ...', ...}] ...
============llm_response type====================
AIMessage
```

## Concept Notes: Output Parsers

### What is a parser?

When a model answers, LangChain gives back an `AIMessage` object. It holds the text, but also metadata such as token usage, so it is not always the easiest thing to work with.

An **output parser** is a step placed after the model in a chain. It takes the raw model response and converts it into a format the rest of the program can use directly, such as a plain string or a validated Python object.

```text
prompt | llm | parser
```

The prompt prepares the input, the model generates the answer, and the parser cleans up the answer.

### 1. String Output Parser

`StrOutputParser` converts the `AIMessage` into a plain Python `str`.

```python
from langchain_core.output_parsers import StrOutputParser

chain = prompt_template | llm | StrOutputParser()
result = chain.invoke({"topic": "SQL", "language": "Hindi", "level": "advanced"})

print(result)        # already a string, no .text or .content needed
```

Use it when:

- The answer is simple text, such as an explanation or a summary
- You want to print the answer or save it directly
- You want to pass the text into the next prompt in a longer chain

### 2. Structured Output Parser

A structured output parser converts the model's text into a validated **Pydantic object** instead of a plain string. `PydanticOutputParser` is the main example.

```python
from langchain_core.output_parsers import PydanticOutputParser

parser = PydanticOutputParser(pydantic_object=Employee)

prompt = PromptTemplate.from_template(
    "Extract the employee details.\n{format_instructions}\n\n{text}",
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | llm | parser
result = chain.invoke({"text": text})   # result is an Employee object
```

How it works:

- `get_format_instructions()` produces text that tells the model which JSON format to return, and this is added to the prompt
- The parser reads the model's JSON response and builds the Pydantic model from it
- If the response does not match the model, parsing fails with an error instead of passing bad data along

Use it when:

- You need specific fields, such as name, technology, or experience
- You want type checks and validation rules on the output
- Other code will use the result as an object, not as free text

This is closely related to `.with_structured_output()` used in projects 5, 6, and 7. Both give validated Pydantic objects. The difference is that `.with_structured_output()` uses the model's built-in structured output support, so no format instructions are needed in the prompt.

### Quick comparison

| | String Output Parser | Structured Output Parser |
|---|---|---|
| Returns | Plain `str` | Pydantic object |
| Validation | None | Types and rules from the model |
| Best for | Explanations, summaries, chat text | Extraction, classification, data for code |
| Fails on bad output | No | Yes, raises a parsing error |

## Setup

### 1. Clone This Repository

```bash
git clone https://github.com/a1108/langchain-learning-journey.git
cd langchain-learning-journey
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Add Your Gemini API Key

Create a `.env` file in the project folder:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

Never upload your `.env` file to GitHub because it contains your private API key.

## Run the Projects

```bash
python static_prompt.py
python dynamic_prompt.py
python travel_guide.py
python pydantic_school.py
python scrapedCandidateEntity.py
```

## Technologies Used

- Python
- LangChain
- Google Gemini API
- Pydantic
- `langchain-google-genai`
- `python-dotenv`

## Next Steps

- Chat messages and system messages
- Multi-step chains
- LangGraph state, nodes, and edges
- AI agents and tool calling

## Note

This repository is part of my practical AI learning journey. Each project is created to understand one concept through hands-on practice.