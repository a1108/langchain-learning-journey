# LangChain Learning Journey

This repository documents my hands-on AI learning journey using Python, LangChain, Google Gemini, and Pydantic.

I am learning to build AI applications step by step: starting with basic prompts, moving to dynamic prompts, output parsing, LCEL chains, multi-step workflows, parallel workflows, and practical mini-projects. My next learning phase will focus on LangGraph workflows and AI agents.

---

## What I Am Learning

- Python virtual environments
- Environment variables and API-key security
- Google Gemini integration with LangChain
- Static prompts
- Dynamic prompts with user input
- Prompt templates
- LangChain Expression Language (LCEL) and chaining with the `|` operator
- Runnable and RunnableSequence concepts
- RunnableLambda for data transformation
- RunnableParallel for parallel execution
- RunnablePassthrough for passing input unchanged
- Output parsers: string output and structured output
- Multi-step chains with multiple LLM calls
- Passing outputs between chain steps
- Parallel branches with independent activities
- Batch processing with `chain.batch()`
- Streaming responses with `chain.stream()`
- System and human messages
- Building practical AI applications
- Pydantic models and data validation

---

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

---

### 2. Dynamic Prompt

File: `dynamic_prompt.py`

This example asks the user for a topic, language, and learning level. It uses LangChain's `PromptTemplate` to create a customized AI prompt.

Example input:

```text
Enter Topic: SQL
Enter Language: Hindi
Enter Level: advanced
```

The values entered by the user are passed to the prompt template and used to generate a customized explanation.

---

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

---

### 4. School Data Validation with Pydantic

File: `pydantic_school.py`

This example uses Pydantic models to validate student, teacher, and school data.

Concepts practiced:

- Creating models with `BaseModel`
- Validating strings and integers with `Field`
- Using `ge`, `le`, and `gt` validation rules
- Creating optional fields with `str | None` and `default=None`
- Using default values
- Creating nested models with `list[Student]` and `list[Teacher]`
- Handling invalid input with `ValidationError`
- Converting a model to a dictionary with `.model_dump()`

Example:

```text
Student:

first_name='Ankit' middle_name='Kumar' last_name='Gupta' age=20 grade='A'

School as dictionary:

{'name': 'DurgaClasses', 'school_id': 101, 'students': [...], 'teachers': [...]}
```

---

### 5. Candidate Profile Extraction (Structured Output)

File: `candidate_extraction.py`

This project parses and scrapes unstructured text from user inputs to extract validated applicant details using Pydantic and Gemini.

Concepts practiced:

- Enforcing JSON schema generation using `.with_structured_output()`
- Parsing raw text directly into structured Pydantic model instances
- Validating extracted employee attributes such as name, technology, and years of experience

Example:

```text
Enter employee information: Ankit began his career at Ericsson, joining as a Java Developer on September 15, 2015.

Employee Details:

name='Ankit'
technology='Java'
experience=11
```

---

### 6. Raw and Structured Output Handling

File: `rawWithStructure.py`

This example demonstrates how to capture and inspect both the raw model output and the validated Pydantic object using the `include_raw=True` option.

Concepts practiced:

- Enabling `include_raw=True` in `.with_structured_output()`
- Accessing raw model output with `result["raw"]`
- Accessing parsed Pydantic objects with `result["parsed"]`
- Accessing runtime parsing errors with `result["parsing_error"]`
- Managing optional fields such as `str | None` and `int | None` with default values of `None`
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

---

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

---

### 8. LangChain Expression Language (LCEL) Chain

File: `lcel_chain.py`

This example asks the user for a topic, language, and learning level, then builds a chain using LangChain Expression Language (LCEL).

A `PromptTemplate` with default values is piped into Gemini with the `|` operator, and the whole chain is run with a single `.invoke()` call.

Concepts practiced:

- Composing components with the LCEL `|` operator (`prompt_template | llm`)
- Setting default values with `partial_variables`
- Overriding those defaults by passing values to `chain.invoke()`
- Running a chain with a dictionary of inputs
- Understanding that LCEL composition creates a `RunnableSequence`
- Comparing the response type (`AIMessage`) with the chain type (`RunnableSequence`)

Example input:

```text
Enter Topic: SQL
Enter Language: Hindi
Enter Level: advanced
```

The script also prints the type names:

```text
AIMessage
RunnableSequence
```

---

### 9. String Output Parser

File: `str_output_parser.py`

This example calls Gemini with a fixed question, then passes the model response through `StrOutputParser` to compare the raw `AIMessage` with the parsed plain string.

Concepts practiced:

- Creating a parser with `StrOutputParser()`
- Running a parser on its own with `parser.invoke(llm_response)`
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

---

### 10. Batch Processing with an LCEL Chain

File: `batch_chain.py`

This example builds a complete chain with a prompt template, Gemini, and `StrOutputParser`, then runs it on several inputs in one call using `.batch()`.

Each input is a topic such as Python, Java, or SQL, and the chain returns one plain-text answer per topic.

Concepts practiced:

- Building a three-step LCEL chain: `prompt_template | llm | parser`
- Setting a default topic with `partial_variables`
- Passing a list of input dictionaries to `chain.batch(inputs)`
- Getting back a list of parsed strings, one per input, in the same order
- Looping over the results to print each answer
- Confirming the types: `list` for the batch response and `RunnableSequence` for the chain

Example output:

```text
<5 short points about Python>
-----------------------------------------------

<5 short points about Java>
-----------------------------------------------

<5 short points about SQL>
-----------------------------------------------

list
RunnableSequence
```

---

### 11. Streaming Responses

File: `stream_chain.py`

This example asks the user for a topic and streams the answer as it is generated, instead of waiting for the full response.

It uses the same `prompt_template | llm | parser` chain and prints each chunk as it arrives with `chain.stream()`.

Concepts practiced:

- Reusing an LCEL chain with `StrOutputParser`, so each chunk is plain text
- Collecting a topic with `input()` and passing it to the chain
- Streaming with `chain.stream()` and looping over the chunks
- Printing chunks as they arrive with `print(chunk, end="", flush=True)`
- Understanding the difference between `.invoke()` (one full response), `.batch()` (many inputs), and `.stream()` (a response in pieces)

Example input:

```text
Enter your topic name: Python
```

---

### 12. Multi-Step RunnableSequence Chain

File: `multi_step_chain.py`

This example demonstrates how to build a multi-step LangChain pipeline using `RunnableSequence`.

The chain performs two LLM calls:

1. The first Gemini model explains a topic for a beginner.
2. The explanation is converted into a string using `StrOutputParser`.
3. `RunnableLambda` transforms the string into the dictionary required by the next prompt.
4. The second Gemini model uses that explanation to generate multiple-choice questions.
5. A second `StrOutputParser` converts the final `AIMessage` into a plain Python string.

This demonstrates how the output of one LLM step can become the input to another LLM step.

Concepts practiced:

- Creating a multi-step chain with `RunnableSequence`
- Calling multiple LLMs sequentially
- Using `StrOutputParser` between LLM steps
- Using `RunnableLambda` for data transformation
- Passing output from one model call into the next prompt
- Building dependent multi-step workflows
- Understanding how data flows between `Runnable` components
- Separating prompt preparation, model execution, parsing, and transformation

#### Chain Flow

```text
Input
  ↓
Explanation Prompt
  ↓
Gemini Model 1
  ↓
StrOutputParser
  ↓
RunnableLambda
  ↓
{"content": explanation}
  ↓
Quiz Prompt
  ↓
Gemini Model 2
  ↓
StrOutputParser
  ↓
Final MCQs
```

The chain is explicitly created using `RunnableSequence`:

```python
chain = RunnableSequence(
    explanation_prompt,
    model1,
    parser,
    prepare_quiz_input,
    quiz_prompt,
    model2,
    parser
)
```

The first model produces an explanation.

`StrOutputParser` converts the `AIMessage` returned by the model into a plain string.

Then `RunnableLambda` transforms that string into the dictionary expected by the next prompt:

```python
prepare_quiz_input = RunnableLambda(
    lambda content: {"content": content}
)
```

The resulting data looks conceptually like:

```text
"Java is a programming language..."
```

becomes:

```python
{
    "content": "Java is a programming language..."
}
```

That dictionary is then consumed by the quiz prompt.

The complete data flow is:

```text
{"topic": "Java"}
      ↓
Explanation Prompt
      ↓
Gemini Model 1
      ↓
AIMessage
      ↓
StrOutputParser
      ↓
"Java is a programming language..."
      ↓
RunnableLambda
      ↓
{"content": "Java is a programming language..."}
      ↓
Quiz Prompt
      ↓
Gemini Model 2
      ↓
AIMessage
      ↓
StrOutputParser
      ↓
Final MCQs
```

The chain is invoked with:

```python
responses = chain.invoke({"topic": "Java"})
```

This example is important because a LangChain workflow does not have to be limited to:

```text
Prompt → Model → Parser
```

It can also contain multiple models and custom transformation steps:

```text
Prompt → Model → Parser → Transform → Prompt → Model → Parser
```

---

### 13. RunnableSequence + RunnableParallel Workflow

File: `runnable_sequence_parallel.py`

This example expands the previous multi-step workflow to demonstrate **parallel execution with `RunnableParallel`**.

The user provides:

- Topic
- Audience

The first LLM generates a **Core Explanation**.

That explanation is then transformed by `RunnableLambda` into the dictionary expected by the parallel branches.

The same input is then sent to multiple independent activities using `RunnableParallel`.

The workflow intentionally includes different activities to demonstrate how parallel branches can perform different tasks using the same input.

#### Learning Goal

Understand how a LangChain workflow can combine:

- `RunnableSequence`
- `RunnableLambda`
- `RunnableParallel`
- `RunnablePassthrough`
- Multiple independent LLM calls

#### Chain Flow

```text
Topic + Audience
       ↓
Explanation Prompt
       ↓
Gemini Model
       ↓
StrOutputParser
       ↓
Core Explanation
       ↓
RunnableLambda
       ↓
{"content": explanation}
       ↓
RunnableParallel
       ├──→ Description
       │       ↓
       │   RunnablePassthrough
       │
       ├──→ Summary
       │       ↓
       │     Gemini
       │
       ├──→ Quiz
       │       ↓
       │     Gemini
       │
       ├──→ Social Post
       │       ↓
       │     Gemini
       │
       └──→ Interview Questions
               ↓
             Gemini
```

#### RunnableParallel

`RunnableParallel` sends the same input to multiple independent branches.

Example:

```python
parallel_stage = RunnableParallel(
    description=RunnablePassthrough(),
    summary=summary_chain,
    quiz=quiz_chain,
    social_post=social_chain,
    interview_questions=interview_chain
)
```

Each branch performs a different activity:

```text
Same Input
    │
    ├──→ Description
    ├──→ Summary
    ├──→ Quiz
    ├──→ Social Post
    └──→ Interview Questions
```

The branches are independent from each other.

#### RunnablePassthrough

`RunnablePassthrough` passes the input forward unchanged.

In this example:

```python
description=RunnablePassthrough()
```

the `description` branch receives the same input that entered `RunnableParallel`.

It does not call the LLM.

Conceptually:

```text
Input
  ↓
RunnablePassthrough
  ↓
Same Input
```

This is useful when one branch needs to preserve the original input while other branches transform or process it.

#### RunnableLambda

Before the parallel stage, `RunnableLambda` converts the explanation string into the dictionary expected by the downstream prompts:

```python
def prepare_input(explanation):
    parallel_input = {
        "content": explanation
    }

    print("\n===== INPUT TO PARALLEL =====")
    print(parallel_input)
    print("=============================\n")

    return parallel_input


prepare_parallel_input = RunnableLambda(prepare_input)
```

This makes the data flow visible during learning.

The data changes from:

```text
"Java is a popular programming language..."
```

to:

```python
{
    "content": "Java is a popular programming language..."
}
```

That dictionary becomes the input to `RunnableParallel`.

#### Complete Pipeline

```python
final_chain = (
    explanation_chain
    | prepare_parallel_input
    | parallel_stage
)
```

Conceptually:

```text
Topic + Audience
       ↓
RunnableSequence
       ↓
Core Explanation
       ↓
RunnableLambda
       ↓
Dictionary Input
       ↓
RunnableParallel
       ├── Summary
       ├── Quiz
       ├── Social Post
       ├── Interview Questions
       └── Description
```

#### Model Call Count

For one call to:

```python
result = final_chain.invoke(
    {
        "topic": topic,
        "audience": audience
    }
)
```

the workflow makes **5 LLM/model calls**:

```text
1. Core Explanation
2. Summary
3. Quiz
4. Social Post
5. Interview Questions
```

`RunnableLambda` does not make an LLM call.

`RunnablePassthrough` does not make an LLM call.

Therefore:

```text
Total LLM calls = 5
```

#### Example Input

```text
Enter topic: Java
Enter audience: Experience
```

#### Example Output

The workflow generates:

```text
SUMMARY
=======
5 short summary points

QUIZ
====
5 beginner multiple-choice questions

SOCIAL POST
===========
A short social-media post

INTERVIEW QUESTIONS
===================
5 interview questions

DESCRIPTION
===========
The original Core Explanation
```

The important concept is that the **same Core Explanation is used as the input for multiple independent activities**.

This demonstrates the difference between sequential and parallel workflows.

Sequential:

```text
A
↓
B
↓
C
```

Parallel:

```text
       ┌→ B
A ─────┼→ C
       └→ D
```

---

## Concept Notes: Output Parsers

### What is a parser?

When a model answers, LangChain gives back an `AIMessage` object. It holds the text, but also metadata such as token usage, so it is not always the easiest thing to work with.

An **output parser** is a step placed after the model in a chain. It takes the raw model response and converts it into a format the rest of the program can use directly, such as a plain string or a validated Python object.

```text
prompt | llm | parser
```

The prompt prepares the input, the model generates the answer, and the parser converts the answer into the required format.

### 1. String Output Parser

`StrOutputParser` converts the `AIMessage` into a plain Python `str`.

```python
from langchain_core.output_parsers import StrOutputParser

chain = prompt_template | llm | StrOutputParser()

result = chain.invoke({
    "topic": "SQL",
    "language": "Hindi",
    "level": "advanced"
})

print(result)
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
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    },
)

chain = prompt | llm | parser

result = chain.invoke({"text": text})
```

Use it when:

- You need specific fields, such as name, technology, or experience
- You want type checks and validation rules on the output
- Other code will use the result as an object, not as free text

This is closely related to `.with_structured_output()` used in projects 5, 6, and 7. Both give validated Pydantic objects.

The difference is that `.with_structured_output()` uses the model's built-in structured output support, so no format instructions are needed in the prompt.

### Quick Comparison

| | String Output Parser | Structured Output Parser |
|---|---|---|
| Returns | Plain `str` | Pydantic object |
| Validation | None | Types and rules from the model |
| Best for | Explanations, summaries, chat text | Extraction, classification, data for code |
| Fails on bad output | No | Yes, raises a parsing error |

---

## Concept Notes: RunnableSequence and RunnableLambda

### RunnableSequence

`RunnableSequence` represents a sequence of Runnable components executed one after another.

For example:

```python
chain = RunnableSequence(
    prompt,
    llm,
    parser
)
```

This is conceptually similar to LCEL composition:

```python
chain = prompt | llm | parser
```

The major idea is that the output of one Runnable becomes the input to the next Runnable.

A more complex sequence can contain multiple models, parsers, and transformation steps:

```text
Runnable
  ↓
Runnable
  ↓
Runnable
  ↓
Runnable
  ↓
Runnable
```

### RunnableLambda

`RunnableLambda` allows normal Python logic to be used as a Runnable inside a LangChain chain.

Example:

```python
prepare_quiz_input = RunnableLambda(
    lambda content: {"content": content}
)
```

It receives the output from the previous step and transforms it into the format required by the next step.

This is useful when the output from one component does not directly match the input expected by the next component.

For example:

```text
Previous step:

"Java is a programming language..."

       ↓

RunnableLambda

       ↓

{
    "content": "Java is a programming language..."
}
```

This allows custom Python transformations to become part of the LangChain pipeline.

---

## Concept Notes: RunnableParallel and RunnablePassthrough

### RunnableParallel

`RunnableParallel` sends the same input to multiple independent Runnable branches.

Example:

```python
parallel_chain = RunnableParallel(
    summary=summary_chain,
    quiz=quiz_chain,
    social_post=social_chain
)
```

Conceptually:

```text
             Same Input
                  │
        ┌─────────┼─────────┐
        ↓         ↓         ↓
     Summary     Quiz    Social Post
```

Each branch can perform a different activity.

A branch containing an LLM makes its own model call.

Therefore, if three branches contain LLMs:

```text
RunnableParallel
   ├── Summary → LLM Call
   ├── Quiz → LLM Call
   └── Social Post → LLM Call
```

there are three LLM calls in the parallel stage.

### RunnablePassthrough

`RunnablePassthrough` passes the input through without changing it.

```python
passthrough = RunnablePassthrough()

result = passthrough.invoke("Hello LangChain")

print(result)
```

Output:

```text
Hello LangChain
```

Conceptually:

```text
Input
  ↓
RunnablePassthrough
  ↓
Same Input
```

It is particularly useful inside `RunnableParallel` when one branch needs to preserve the original input while other branches perform processing.

Example:

```python
parallel_chain = RunnableParallel(
    original=RunnablePassthrough(),
    processed=some_chain
)
```

Conceptually:

```text
                 Input
                   │
          ┌────────┴────────┐
          ↓                 ↓
 RunnablePassthrough     some_chain
          ↓                 ↓
     Original           Processed
```

### RunnableParallel vs RunnableSequence

The key difference is the direction of data flow.

`RunnableSequence`:

```text
A
↓
B
↓
C
```

Output from one step becomes input to the next step.

`RunnableParallel`:

```text
        ┌→ B
A ──────┼→ C
        └→ D
```

The same input is sent to multiple independent branches.

### Combined Workflow

The concepts can be combined:

```text
Topic + Audience
       ↓
RunnableSequence
       ↓
Core Explanation
       ↓
RunnableLambda
       ↓
Dictionary
       ↓
RunnableParallel
    ┌──┼────┬───────┐
    ↓  ↓    ↓       ↓
 Summary Quiz Social Interview
```

This gives a workflow containing both sequential and parallel processing.

---

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

---

## Run the Projects

```bash
python static_prompt.py
python dynamic_prompt.py
python travel_guide.py
python pydantic_school.py
python scrapedCandidateEntity.py
python lcel_chain.py
python str_output_parser.py
python batch_chain.py
python stream_chain.py
python multi_step_chain.py
python runnable_sequence_parallel.py
```

---

## Technologies Used

- Python
- LangChain
- Google Gemini API
- Pydantic
- `langchain-google-genai`
- `python-dotenv`

---

## Next Steps

- Chat messages and system messages
- More complex multi-step chains
- More LCEL composition patterns
- LangGraph state, nodes, and edges
- AI agents and tool calling

---

## Note

This repository is part of my practical AI learning journey. Each project is created to understand one concept through hands-on practice.