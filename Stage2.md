# Enterprise Document Chatbot using RAG — Stage 2

## Project Overview

Enterprise Document Chatbot is an AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload enterprise PDF documents and interact with them using natural language queries.

The system performs semantic document retrieval using FAISS vector search and generates context-aware answers using OpenAI GPT models.

Stage 2 focuses on transforming the basic RAG prototype into a more enterprise-style AI application with dynamic document upload, optimized workflows, conversational UI, and observability using LangSmith.

---

# Features Implemented in Stage 2

## Dynamic PDF Upload

- Users can upload PDF documents directly from the Streamlit frontend
- Supports multiple PDF uploads
- Automatically processes newly uploaded documents
- Prevents unnecessary reprocessing of existing documents

---

## Automated RAG Pipeline

After upload, the system automatically:

1. Loads PDF documents
2. Splits documents into chunks
3. Generates OpenAI embeddings
4. Stores embeddings in FAISS vector database
5. Updates semantic retriever

---

## Conversational Chat Interface

- ChatGPT-style interface using Streamlit
- Session-based chat history
- Interactive conversational flow
- Real-time question answering

---

## Semantic Search using FAISS

- Retrieves contextually relevant chunks
- Uses vector similarity search
- Enables enterprise document querying

---

## GPT-Powered Response Generation

- OpenAI GPT integrated using LangChain
- Generates context-aware responses
- Uses retrieved document chunks for grounded answers

---

## Source Citation Support

Each answer includes:

- Source document name
- Page number references

This improves explainability and transparency.

---

## FastAPI Backend APIs

Implemented REST APIs for chatbot interaction.

### Available Endpoint

```http
POST /chat
```

Used by Streamlit frontend for communication with backend RAG system.

---

## LangSmith Tracing & Observability

Integrated LangSmith for:

- LLM execution tracing
- Retrieval debugging
- Token monitoring
- Latency analysis
- Prompt inspection

---

## Optimized Document Processing Workflow

Implemented workflow optimization to ensure:

✅ Documents process only during upload  
✅ Questions do not trigger re-ingestion  
✅ Faster response generation  
✅ Better application performance  

---

# Technologies Used

## Backend
- Python
- FastAPI
- LangChain
- OpenAI API
- FAISS

## Frontend
- Streamlit

## AI / Retrieval
- OpenAI Embeddings
- GPT Models
- Vector Similarity Search

## Monitoring
- LangSmith

---

# Project Architecture

```text
                ┌────────────────────┐
                │  Streamlit Frontend │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ PDF Upload Manager │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Ingestion Pipeline │
                └─────────┬──────────┘
                          │
         ┌────────────────┼────────────────┐
         ▼                ▼                ▼
 ┌─────────────┐  ┌──────────────┐  ┌────────────┐
 │ Chunking    │  │ Embeddings   │  │ Metadata   │
 └─────────────┘  └──────────────┘  └────────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ FAISS Vector Store │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Semantic Retriever │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ OpenAI GPT Model   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ FastAPI Backend    │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Streamlit Response │
                └────────────────────┘
```

---

# Workflow

## Step 1 — Upload Documents

Users upload enterprise PDF files from the Streamlit sidebar.

---

## Step 2 — Document Processing

The system:

- Loads PDFs
- Splits text into chunks
- Generates embeddings
- Updates FAISS vector store

---

## Step 3 — Ask Questions

Users ask natural language questions through chat interface.

---

## Step 4 — Semantic Retrieval

Relevant document chunks are retrieved using vector similarity search.

---

## Step 5 — GPT Answer Generation

Retrieved context is passed to OpenAI GPT model to generate grounded answers.

---

## Step 6 — Display Results

Chatbot displays:

- AI-generated answer
- Source document references

---

# Folder Structure

```text
enterprise-rag-chatbot/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   └── rag/
│       ├── __init__.py
│       ├── ingest.py
│       ├── retriever.py
│       └── generator.py
│
├── data/
│   ├── pdfs/
│   └── vector_store/
│
├── streamlit_app/
│   ├── __init__.py
│   └── ui.py
│
├── .env
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your-github-repo-url>

cd enterprise-rag-chatbot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create `.env`

```env
OPENAI_API_KEY=your_openai_api_key

LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=enterprise-rag-chatbot
```

---

# Running the Project

## Step 1 — Start FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## Step 2 — Start Streamlit Frontend

Open a new terminal:

```bash
streamlit run streamlit_app/ui.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# How to Use

## Upload Documents

- Open Streamlit UI
- Upload one or more PDF files
- Wait for processing completion

---

## Ask Questions

Example questions:

```text
What is cloud computing?

What are the advantages of AWS?

Explain the deployment models.
```

---

# Example Features

✅ Multi-document support  
✅ Conversational chat UI  
✅ Source-aware responses  
✅ Dynamic document ingestion  
✅ Enterprise-style architecture  
✅ LangSmith tracing  
✅ FastAPI APIs  
✅ Semantic search  

---

# Future Enhancements

- Streaming responses
- LangGraph workflows
- Memory integration
- Hybrid retrieval
- OCR support
- Docker deployment
- Cloud deployment
- Authentication & RBAC
- Multi-user support
- Advanced prompt engineering

---

# Author

Bhavana
