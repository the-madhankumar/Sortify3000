import chromadb


client = chromadb.Client()
collection = client.create_collection(name="vector_data")

def store_embedding(embedding: list[float], doc_id: str, metadata: dict[str, str]):
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
