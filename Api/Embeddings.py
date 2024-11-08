import os
import pdfplumber
from pptx import Presentation
import pandas as pd
from langchain.embeddings import HuggingFaceBgeEmbeddings
from transformers import AutoTokenizer
from VectorData import store_embedding

embeddings = HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def read_document(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    text = ""

    if ext == ".pdf":
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    elif ext == ".pptx":
        prs = Presentation(file_path)
        for slide in prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    text += shape.text + ' '
    elif ext in ['.xls', '.xlsx']:
        df = pd.read_excel(file_path)
        text = df.to_string(index=False)
    else:
        with open(file_path, 'r') as file:
            text = file.read()
    
    return text

def create_document_embedding(document_text):
    document_embedding = embeddings.embed_documents([document_text])[0]
    return document_embedding

file_path = r"C:\Users\madha\Downloads\qbmin.pdf" 
document_text = read_document(file_path)

document_embedding = create_document_embedding(document_text)

doc_id = f"doc_{os.path.basename(file_path)}"
metadata = {"file_path": file_path}

store_embedding(document_embedding, doc_id, metadata)

print("Document embedding stored successfully.")
