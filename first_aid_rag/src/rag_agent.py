import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

def setup_rag_agent(pdf_path: str = 'data/FA-manual.pdf'):
    api_key = os.environ.get('GROQ_API_KEY')
    if not api_key:
        raise EnvironmentError('Groq api key is not present.')

    if not os.path.exists(pdf_path):
        raise FileNotFoundError('Pdf file does not exists.')

    try:
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )
        split_docs = text_splitter.split_documents(documents)

        embeddings = HuggingFaceEmbeddings(model_name = 'all-MiniLM-L6-v2')

        vector_store = FAISS.from_documents(split_docs, embeddings)

        prompt_template = """You are a helpful first-aid assistant. Use the context provided to answer user's question
        Context: {context}
        Question: {question}
        Answer:
        """

        qa_prompt = PromptTemplate(input_variables = ['context', 'question'], template = prompt_template)

        llm = ChatGroq(model_name = 'llama3-8b-8192', api_key = os.environ.get('GROQ_API_KEY'))

        retrieval_qa_chain = RetrievalQA.from_chain_type(
            llm = llm,
            chain_type = 'stuff',
            retriever = vector_store.as_retriever(search_type = 'similarity', search_kwargs = {'k': 5}),
            return_source_documents = True,
            chain_type_kwargs = {'prompt': qa_prompt}
        )
        return retrieval_qa_chain
    except Exception as e:
        raise RuntimeError(f'Error during RAG setup: {e}')

def generate_response(retrieval_qa_chain, query):
    if retrieval_qa_chain is None:
        raise ValueError('No retrieval chain set up.')
    
    try:
        query = " ".join(query) if isinstance(query, list) else query
        result = retrieval_qa_chain(query)
        answer = result['result']

        return answer
    except Exception as e:
        raise RuntimeError(f'Error while generating response: {e}')