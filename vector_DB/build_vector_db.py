import os 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import(Chroma)
from langchain_huggingface import(HuggingFaceEmbeddings)
from pypdf import PdfReader
from docx import Document

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

KB_PATH = os.path.join(BASE_DIR,"knowledge_base")

kb_path = KB_PATH

CHROMA_PATH = os.path.join(BASE_DIR,"vector_db","chroma_db")

def load_documents():
    documents=[]
    kb_path = KB_PATH
    for root,_,files in os.walk(kb_path):
        for file in files:
            file_path = os.path.join(root,file)
            text=""
            print(f"Searching in: {kb_path}")
            print(f"Found file: {file_path}")
            try:
                if file.endswith('.txt'):
                    with open(file_path,'r',encoding='utf-8') as f:
                        text=f.read()

                elif file.endswith('.pdf'):
                    reader = PdfReader(file_path)
                    for page in reader.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text+=page_text+'\n'

                elif file.endswith('.docx'):
                    doc = Document(file_path)
                    for para in doc.paragraphs:
                        if para.text.strip():
                            text+=para.text+"\n"
                
                if text.strip():
                    documents.append(text)

            except Exception as e:
                print(f'Error reading {file_path}:{str(e)}')
    
    return documents



def chunk_documents(documents):
    splitter=(RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100))
    chunks=[]
    for doc in documents:
        chunks.extend(
            splitter.split_text(doc)
        )
    return chunks



def build_vector_db():
    docs=load_documents()
    chunks=chunk_documents(docs)
    print(f'Loaded {len(chunks)} chunks')

    embeddings=(
        HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    )

    if not chunks:
        raise ValueError("No chunks created. Check knowledge_base path.")

    vector_db = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )
    #vector_db.persist()

    print("Vector DB created Successfully")

if __name__=='__main__':
    build_vector_db()

