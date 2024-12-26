import gradio as gr
from src.rag_agent import setup_rag_agent, generate_response

retrieval_qa_chain = setup_rag_agent()

def handle_query(query, history):
    response = generate_response(retrieval_qa_chain, query)

    return response

interface = gr.ChatInterface(
    fn = handle_query,
    type = 'messages',
    title = 'First-Aid Assistant',
    description= 'Ask questions about first aid and preliminary treatment.',
    theme=gr.themes.Base()
)