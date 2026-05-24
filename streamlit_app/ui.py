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


# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="Enterprise RAG Chatbot",
    layout="wide"
)


# -----------------------------------
# Session State
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []


# -----------------------------------
# Sidebar
# -----------------------------------

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

                st.success(
                    f"Uploaded: {uploaded_file.name}"
                )

                new_files_uploaded = True

        # Process documents ONLY once
        if new_files_uploaded:

            with st.spinner("Processing documents..."):

                ingest_documents()

            st.success(
                "Documents processed successfully"
            )

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


# -----------------------------------
# Main Chat UI
# -----------------------------------

st.title("Enterprise Document Chatbot")

st.write(
    "Ask questions from your uploaded enterprise documents."
)


# -----------------------------------
# Display Previous Messages
# -----------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# -----------------------------------
# Chat Input
# -----------------------------------

question = st.chat_input(
    "Ask a question about your documents"
)


if question:

    # Prevent asking without PDFs
    if not st.session_state.uploaded_files:

        st.warning(
            "Please upload at least one PDF first."
        )

    else:

        # -----------------------------------
        # User Message
        # -----------------------------------

        with st.chat_message("user"):

            st.markdown(question)

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        # -----------------------------------
        # Assistant Response
        # -----------------------------------

        with st.chat_message("assistant"):

            response_placeholder = st.empty()

            full_response = ""

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "question": question
                    },
                    stream=True
                )

                if response.status_code != 200:

                    st.error(
                        f"Backend Error: "
                        f"{response.status_code}"
                    )

                else:

                    for chunk in response.iter_content(
                        chunk_size=1,
                        decode_unicode=True
                    ):

                        if chunk:

                            full_response += chunk

                            response_placeholder.markdown(
                                full_response + "▌"
                            )

                    response_placeholder.markdown(
                        full_response
                    )

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": full_response
                    })

            except Exception as e:

                st.error(f"Error: {e}")