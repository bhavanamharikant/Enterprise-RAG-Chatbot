from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain_classic.chains import RetrievalQA

from app.rag.retriever import get_vector_store


load_dotenv()


def get_qa_chain():

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    vector_store = get_vector_store()

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True
    )

    return qa_chain


if __name__ == "__main__":

    qa_chain = get_qa_chain()

    while True:

        question = input("\nAsk a question (or type 'exit'): ")

        if question.lower() == "exit":
            break

        response = qa_chain.invoke({"query": question})

        print("\nAnswer:")
        print(response["result"])

        print("\nSources Used:")
        print("-" * 50)

        for i, doc in enumerate(response["source_documents"], start=1):

            source = doc.metadata.get("source", "Unknown")

            page = doc.metadata.get("page", "N/A")

            print(f"{i}. File: {source} | Page: {page}")