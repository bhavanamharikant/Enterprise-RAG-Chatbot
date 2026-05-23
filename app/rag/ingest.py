import os 
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

PDF_DIR="data/pdfs/"
VECTOR_DB_PATH="data/vector_store"

def load_documents():

    documents = []

    for file in os.listdir(PDF_DIR):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(PDF_DIR, file)

            loader = PyPDFLoader(pdf_path)

            docs = loader.load()

            documents.extend(docs)

            print(f"Loaded: {file}")

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    return chunks


def create_vector_store(chunks):

    embeddings = OpenAIEmbeddings()

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_store.save_local(VECTOR_DB_PATH)

    print("Vector store updated successfully")


def ingest_documents():

    documents = load_documents()

    chunks = split_documents(documents)

    create_vector_store(chunks)


if __name__ == "__main__":

    ingest_documents()