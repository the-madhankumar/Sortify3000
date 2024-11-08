import chromadb
from chromadb.client import Client
from chromadb.scheme import Collection


client = chromadb.Client()
collection = client.create_collection(name="vector_data")

def store_embedding(embedding: List[float], doc_id: str, metadata: Dict[str, str]):
    try:
        collection.add(
            embeddings=[embedding],
            metadatas=[metadata],
            ids=[doc_id]
        )
        import json
        result = {
            "success": True,
            "message": "Embedding stored successfully"
        }
        print(json.dumps(result, indent=4))
    except:
        print("Error storing embedding")
