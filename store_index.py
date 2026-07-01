from dotenv import load_dotenv
import os
load_dotenv()
from src.helper import load_pdf_files, filter_to_minimal_docs, text_split, download_embeddings, download_HuggingFaceEmbeddings
from pinecone import Pinecone
from pinecone.models import ServerlessSpec

from langchain_pinecone import PineconeVectorStore


PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY 


extracted_data = load_pdf_files("Data")
minimal_docs= filter_to_minimal_docs(extracted_data)
texts_chunks = text_split(minimal_docs)

embedding =download_HuggingFaceEmbeddings()

pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)


index_name = "medimind"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
index = pc.Index(index_name)


docsearch = PineconeVectorStore.from_documents(
    documents=texts_chunks,
    embedding=embedding,
    index_name=index_name
) 