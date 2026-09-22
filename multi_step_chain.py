from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableSequence

load_dotenv()

model1 = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

model2 = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

parser = StrOutputParser()

explanation_prompt = PromptTemplate.from_template(
    """
    Explain {topic} for a beginner.

    Use very simple English.
    Give one real-world example.
    """
)

prepare_quiz_input = RunnableLambda(
           lambda content: {"content":content}
		   )

quiz_prompt = PromptTemplate.from_template(
    """
    Based only on the following content,
    generate 2 MCQs.

    Content:

    {content}
    """
)

chain = RunnableSequence(explanation_prompt ,model1 , parser , prepare_quiz_input , quiz_prompt, model2, parser)
responses = chain.invoke({"topic":"Java"})
print(responses)