import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/chat"


st.set_page_config(
    page_title="Enterprise RAG Chatbot",
    layout="wide"
)


st.title("Enterprise Document Chatbot")


st.write("Ask questions from your enterprise PDF documents")


question = st.text_input(
    "Enter your question"
)


if st.button("Ask"):

    if question.strip() == "":

        st.warning("Please enter a question")

    else:

        with st.spinner("Generating answer..."):

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "question": question
                    }
                )

                data = response.json()

                st.subheader("Answer")

                st.write(data["answer"])

                st.subheader("Sources")

                for source in data["sources"]:

                    st.write(
                        f"File: {source['source']} | "
                        f"Page: {source['page']}"
                    )

            except Exception as e:

                st.error(f"Error: {e}")