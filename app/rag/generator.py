from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from app.rag.retriever import get_vector_store


load_dotenv()


def get_conversation_chain():

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        streaming=True
    )

    vector_store = get_vector_store()

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 6}
    )

    memory=ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )


    conversation_chain=ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )

    return conversation_chain