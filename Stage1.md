# Enterprise Document Chatbot using RAG — Stage 1

## Project Overview

The Enterprise Document Chatbot is an AI-powered application that allows users to ask questions from enterprise PDF documents using natural language. The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant document content and generate intelligent answers using OpenAI language models.

The application is designed with a modular enterprise-style architecture consisting of:

* Streamlit frontend for user interaction
* FastAPI backend for API communication
* LangChain for RAG pipeline orchestration
* FAISS vector database for semantic search
* OpenAI embeddings and GPT models for intelligent response generation

---

# Objective of Stage 1

The goal of Stage 1 was to build the core end-to-end RAG pipeline capable of:

1. Reading PDF documents
2. Converting documents into embeddings
3. Storing embeddings in a vector database
4. Performing semantic similarity search
5. Generating AI-based responses using retrieved context
6. Exposing the system through APIs
7. Building a functional chatbot frontend

---

# Technologies Used

* Python
* Streamlit
* FastAPI
* LangChain
* OpenAI API
* FAISS
* PyPDF
* LangSmith (environment setup completed)

---

# Architecture Implemented in Stage 1

User Question
↓
Streamlit Frontend
↓
FastAPI Backend
↓
LangChain RAG Pipeline
↓
FAISS Vector Retrieval
↓
OpenAI GPT Response Generation
↓
Response Returned to User

---

# Features Implemented in Stage 1

## 1. PDF Document Ingestion

* Uploaded enterprise PDF documents
* Extracted text using PyPDFLoader
* Loaded multiple PDF files dynamically

### Implemented File

* `app/rag/ingest.py`

---

## 2. Document Chunking

* Split large PDF content into smaller chunks
* Used RecursiveCharacterTextSplitter
* Configured chunk overlap for better context retention

### Benefits

* Improved retrieval accuracy
* Better semantic understanding

---

## 3. Embedding Generation

* Generated vector embeddings using OpenAI Embeddings API
* Converted text chunks into high-dimensional semantic vectors

---

## 4. FAISS Vector Database Integration

* Stored embeddings in FAISS vector store
* Enabled fast semantic similarity search
* Saved vector indexes locally for reuse

### Output Generated

* `index.faiss`
* `index.pkl`

---

## 5. Semantic Retrieval System

* Implemented similarity-based document retrieval
* Retrieved top relevant chunks for user questions
* Tested retrieval quality successfully

### Implemented File

* `app/rag/retriever.py`

---

## 6. GPT-based Answer Generation

* Integrated OpenAI GPT model using LangChain
* Combined retrieved context with user query
* Generated context-aware intelligent answers

### Implemented File

* `app/rag/generator.py`

---

## 7. Source Citation Support

* Displayed source document names and page numbers
* Improved answer transparency and explainability

---

## 8. FastAPI Backend Development

* Built REST API endpoints for chatbot interaction
* Added request/response schema handling
* Enabled external frontend integration

### Implemented Endpoint

* `/chat`

### Implemented File

* `app/main.py`

---

## 9. Streamlit Frontend Development

* Built interactive chatbot interface
* Added question input and answer display
* Integrated frontend with FastAPI backend

### Implemented File

* `streamlit_app/ui.py`

---

## 10. Conversational Chat Interface

* Added session-based chat history
* Implemented ChatGPT-style conversational UI
* Stored previous user and assistant messages

---

# Workflow Executed in Stage 1

## Step 1 — PDF Loading

Enterprise PDF documents were loaded from the local directory.

## Step 2 — Text Chunking

Large document text was divided into smaller overlapping chunks.

## Step 3 — Embedding Creation

OpenAI embeddings converted chunks into semantic vectors.

## Step 4 — Vector Storage

Embeddings were stored inside FAISS vector database.

## Step 5 — User Query Input

User asked questions through Streamlit UI.

## Step 6 — Semantic Retrieval

Relevant chunks were retrieved using vector similarity search.

## Step 7 — LLM Response Generation

Retrieved chunks were passed to GPT model to generate answers.

## Step 8 — Response Display

Final answer and source citations were shown in the chatbot UI.

---

# Commands to Run the Project

## 1. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run PDF Ingestion Pipeline

This converts PDFs into embeddings and stores them in FAISS.

```bash
python app/rag/ingest.py
```

---

## 4. Run FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger API Docs:

```text
http://127.0.0.1:8000/docs
```

---

## 5. Run Streamlit Frontend

Open a new terminal and run:

```bash
streamlit run streamlit_app/ui.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# Outcome of Stage 1

Successfully developed a fully functional RAG-based enterprise document chatbot capable of:

* Answering questions from PDF documents
* Performing semantic search
* Generating AI-based contextual responses
* Providing source-aware answers
* Supporting conversational interaction

The system now serves as the foundational architecture for advanced enterprise AI enhancements in later stages.

---

# Planned Enhancements for Future Stages

* PDF upload from UI
* LangGraph workflow orchestration
* LangSmith tracing and monitoring
* Streaming responses
* Authentication and role-based access
* Multi-user support
* Docker deployment
* Cloud deployment
* Hybrid search and reranking
* Memory integration
* OCR support for scanned PDFs
