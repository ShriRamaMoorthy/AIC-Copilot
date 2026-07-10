from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0
)

def ask_llm(prompt):
    response = llm.invoke(prompt)
    return response.content