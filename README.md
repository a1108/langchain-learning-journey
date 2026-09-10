# LangChain Learning Journey

This repository documents my hands-on AI learning journey using Python, LangChain, and Google Gemini.

I am learning how to build AI applications step by step: starting with basic prompts, moving to dynamic prompts, and building practical mini-projects. My next learning phase will focus on LangGraph workflows and agents.

## What I am learning

- Python virtual environments
- Environment variables and API-key security
- Google Gemini integration with LangChain
- Static prompts
- Dynamic prompts with user input
- Prompt templates
- System and human messages
- Building practical AI applications

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

## Setup

### 1. Clone this repository

```bash
git clone https://github.com/a1108/langchain-learning-journey.git
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

### 4. Add your Gemini API key

Create a `.env` file in the project folder:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

Never upload your `.env` file to GitHub because it contains a private API key.

## Run the projects

```bash
python static_prompt.py
python dynamic_prompt.py
python travel_guide.py
```

## Technologies Used

- Python
- LangChain
- Google Gemini API
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