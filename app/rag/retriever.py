from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

VECTOR_DB_PATH="data/vector_store"

def get_vector_store():
    embeddings=OpenAIEmbeddings()

    vector_store=FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store


def retrieve_documents(query):

    vectore_store=get_vector_store()

    retriever=vectore_store.as_retriever(
        search_kwargs={"k":10}
    )

    results=retriever.invoke(query)

    return results


if __name__=="__main__":
    query=input("Enter your question:")
    documents=retrieve_documents(query)

    print("\n Top Retrived Chunks:\n")

    for i,doc in enumerate(documents,start=1):
        print(f"Result {i}")
        print("-"*50)
        print(doc.page_content)
        print("\n")