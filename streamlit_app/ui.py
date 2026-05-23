import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st
import requests

from app.rag.ingest import ingest_documents


API_URL = "http://127.0.0.1:8000/chat"


st.set_page_config(
    page_title="Enterprise RAG Chatbot",
    layout="wide"
)


# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.header("📂 Upload Documents")

    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        new_files_uploaded = False

        for uploaded_file in uploaded_files:

            if uploaded_file.name not in st.session_state.uploaded_files:

                save_path = os.path.join(
                    "data/pdfs",
                    uploaded_file.name
                )

                with open(save_path, "wb") as f:

                    f.write(uploaded_file.getbuffer())

                st.session_state.uploaded_files.append(
                    uploaded_file.name
                )

                st.success(f"Uploaded: {uploaded_file.name}")

                new_files_uploaded = True


        # Process ONLY if new files added
        if new_files_uploaded:

            with st.spinner("Processing documents..."):

                ingest_documents()

            st.success("Documents processed successfully")


    st.divider()

    st.subheader("Uploaded Documents")

    if st.session_state.uploaded_files:

        for file in st.session_state.uploaded_files:

            st.write(f"✅ {file}")

        st.info(
            f"Total Documents: "
            f"{len(st.session_state.uploaded_files)}"
        )

    else:

        st.warning("No documents uploaded")


# -----------------------------
# Main Chat UI
# -----------------------------

st.title("Enterprise Document Chatbot")

st.write(
    "Ask questions from your uploaded enterprise documents."
)


# Display previous chat messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# Chat Input
question = st.chat_input(
    "Ask a question about your documents"
)


if question:

    # Prevent chat without documents
    if not st.session_state.uploaded_files:

        st.warning(
            "Please upload at least one PDF document first."
        )

    else:

        # Show user message
        with st.chat_message("user"):

            st.markdown(question)

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        # Generate Answer
        with st.chat_message("assistant"):

            with st.spinner("Generating answer..."):

                try:

                    response = requests.post(
                        API_URL,
                        json={
                            "question": question
                        }
                    )

                    data = response.json()

                    answer = data["answer"]

                    st.markdown(answer)

                    # Sources
                    with st.expander("View Sources"):

                        for source in data["sources"]:

                            st.write(
                                f"📄 {source['source']} "
                                f"(Page {source['page']})"
                            )

                    final_response = answer

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": final_response
                    })

                except Exception as e:

                    st.error(f"Error: {e}")