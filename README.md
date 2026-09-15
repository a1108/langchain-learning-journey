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
- Output parsers
- Chains
- LangGraph state, nodes, and edges
- AI agents and tool calling

## Note

This repository is part of my practical AI learning journey. Each project is created to understand one concept through hands-on practice.