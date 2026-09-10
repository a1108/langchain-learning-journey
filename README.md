# LangChain Learning Journey

This repository documents my practical learning journey with **LangChain** and **Google Gemini** using Python.

The goal is to understand how AI applications work step by step: from sending a simple fixed prompt to building dynamic, reusable prompts. 

## What I learned

- Loading secret API keys using environment variables
- Connecting Google Gemini with LangChain
- Sending prompts with `.invoke()`
- Reading AI responses
- Understanding the `AIMessage` response type
- Creating dynamic prompts with `PromptTemplate`
- Accepting user input for topic, language, and difficulty level

## Project files

### `static_prompt.py`

A beginner-friendly example that sends one fixed question to Gemini.

It demonstrates:

- Loading the Gemini API key from `.env`
- Creating a `ChatGoogleGenerativeAI` model
- Sending a static prompt
- Printing the response content
- Printing the response class name

### `dynamic_prompt.py`

An interactive example that creates a prompt from user input.

The program asks for:

- Topic
- Language
- Learning level

It then uses `PromptTemplate` to generate a custom prompt and sends it to Gemini.

Example input:

```text
Enter Topic: SQL
Enter Language: Hindi
Enter Level: advanced
```

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd langchain-learning-journey
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a file named `.env` in the project folder:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

Do not upload `.env` to GitHub. It contains your private API key.

## Run the examples

Run the static prompt example:

```bash
python static_prompt.py
```

Run the dynamic prompt example:

```bash
python dynamic_prompt.py
```

## Technologies used

- Python
- LangChain
- Google Gemini API
- `langchain-google-genai`
- `python-dotenv`

## Next steps

I plan to continue learning:

- System messages and chat messages
- Prompt engineering
- Output parsers
- Chains
- LangGraph workflows
- AI agents and tool calling

## Note

This repository is part of my hands-on AI learning journey. Each example is created to help me understand the practical foundations of building AI applications.
