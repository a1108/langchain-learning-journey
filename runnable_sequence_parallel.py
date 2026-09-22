from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough
)

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)


parser = StrOutputParser()

# ----------------------------------
# STEP 1 — CORE EXPLANATION
# ----------------------------------

explanation_prompt = PromptTemplate.from_template(
    """
    Explain {topic} for {audience}.

    Requirements:
    - Use very simple English
    - Give a clear definition
    - Give 5 key points
    - Give one real-world example
    """
)

explanation_chain = (
    explanation_prompt
    | model
    | parser
)

# ----------------------------------
# Convert String → Dictionary
# ----------------------------------

prepare_parallel_input = RunnableLambda(
    lambda explanation: {
        "content": explanation
    }
)

# ----------------------------------
# SUMMARY BRANCH
# ----------------------------------

summary_prompt = PromptTemplate.from_template(
    """
    Summarize the following content
    in 5 short bullet points:

    {content}
    """
)

summary_chain = (
    summary_prompt
    | model
    | parser
)

# ----------------------------------
# QUIZ BRANCH
# ----------------------------------

quiz_prompt = PromptTemplate.from_template(
    """
    Generate 5 beginner MCQs
    based only on this content:

    {content}

    Give four options and the correct answer.
    """
)

quiz_chain = (
    quiz_prompt
    | model
    | parser
)

# ----------------------------------
# SOCIAL POST BRANCH
# ----------------------------------

social_prompt = PromptTemplate.from_template(
    """
    Create a short social-media post
    from the following content:

    {content}

    Keep it simple and engaging.
    """
)

social_chain = (
    social_prompt
    | model
    | parser
)

# ----------------------------------
# INTERVIEW QUESTIONS BRANCH
# ----------------------------------

interview_prompt = PromptTemplate.from_template(
    """
    Generate 5 beginner interview questions
    from the following content:

    {content}
    """
)

interview_chain = (
    interview_prompt
    | model
    | parser
)

# ----------------------------------
# PARALLEL STAGE
# ----------------------------------

parallel_stage = RunnableParallel(
    description = RunnablePassthrough(),
    summary=summary_chain,
    quiz=quiz_chain,
    social_post=social_chain,
    interview_questions=interview_chain
)

# ----------------------------------
# COMPLETE PIPELINE
# ----------------------------------

final_chain = (
    explanation_chain
    | prepare_parallel_input
    | parallel_stage
)

# ----------------------------------
# USER INPUT
# ----------------------------------

topic = input("Enter topic: ")
audience = input("Enter audience: ")

# ----------------------------------
# EXECUTE
# ----------------------------------

result = final_chain.invoke(
    {
        "topic": topic,
        "audience": audience
    }
)

# ----------------------------------
# DISPLAY
# ----------------------------------

print("\n================================")
print("SUMMARY")
print("================================")
print(result["summary"])

print("\n================================")
print("QUIZ")
print("================================")
print(result["quiz"])

print("\n================================")
print("SOCIAL POST")
print("================================")
print(result["social_post"])

print("\n================================")
print("INTERVIEW QUESTIONS")
print("================================")
print(result["interview_questions"])
print("================================")
print(result["description"]["content"])
