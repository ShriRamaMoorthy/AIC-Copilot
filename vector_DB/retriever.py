from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

CHROMA_PATH = os.path.join(BASE_DIR,"vector_db","chroma_db")

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_db = Chroma(persist_directory=CHROMA_PATH,embedding_function=embeddings)

def retrieve_context(query,k=5):
    docs = vector_db.max_marginal_relevance_search(query,k=k,fetch_k=20)
    return "\n\n".join(doc.page_content for doc in docs)