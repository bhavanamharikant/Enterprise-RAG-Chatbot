from typing import TypedDict

from langgraph.graph import StateGraph, END

from app.rag.generator import get_conversation_chain


# -----------------------------------
# Graph State
# -----------------------------------

class GraphState(TypedDict):

    question: str

    answer: str

    sources: list


# -----------------------------------
# RAG Node
# -----------------------------------

def retrieve_and_generate(state):

    question = state["question"]

    conversation_chain = get_conversation_chain()

    response = conversation_chain.invoke({
        "question": question
    })

    return {

        "answer": response["answer"],

        "sources": [
            {
                "source": doc.metadata.get("source"),
                "page": doc.metadata.get("page")
            }
            for doc in response["source_documents"]
        ]
    }


# -----------------------------------
# Build Graph
# -----------------------------------

workflow = StateGraph(GraphState)

workflow.add_node(
    "rag_pipeline",
    retrieve_and_generate
)

workflow.set_entry_point(
    "rag_pipeline"
)

workflow.add_edge(
    "rag_pipeline",
    END
)

graph = workflow.compile()