import chromadb
import json

client = chromadb.Client()
collection = client.create_collection(name="vector_data")

def store_embedding(embedding: list[float], doc_id: str, metadata: dict[str, str]):
    try:
        for i, embeddings in enumerate(embedding):
            metadata_with_chunk = metadata.copy()
            metadata_with_chunk.update({"doc_id": doc_id, "chunk_index": i})
            collection.add(
                embeddings=[embedding],
                metadatas=[metadata],
                ids=[doc_id]
            )
        result = {
            "success": True,
            "message": "Embedding stored successfully"
        }
        print(json.dumps(result, indent=4))
    except:
        print("Error storing embedding")
