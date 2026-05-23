import os 
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

PDF_DIR="data/pdfs/"
VECTOR_DB_PATH="data/vector_store"

def load_document():
    document=[]

    for file in os.listdir(PDF_DIR):
        if file.endswith(".pdf"):
            pdf_path=os.path.join(PDF_DIR,file)
            loader=PyPDFLoader(pdf_path)
            docs=loader.load()
            document.extend(docs)

            print(f"Loaded: {file}")

    return document

def split_documents(documents):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks=text_splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    return chunks

def create_vector_store(chunks):
    embeddings=OpenAIEmbeddings()
    vector_store=FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_store.save_local(VECTOR_DB_PATH)

    print("FAISS vector store created successfully")


def main():
    print("Loading pedf documents..")
    documents=load_document()

    print("Splitting documents into chunks..")
    chunks=split_documents(documents)

    create_vector_store(chunks)
    print("Ingestion completed successfully")

if __name__=="__main__":
    main()