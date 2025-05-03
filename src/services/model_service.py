from werkzeug.datastructures import FileStorage
from sentence_transformers import SentenceTransformer
from src.config import EMBEDDINGS_FILE, SIMILARITY_THRESHOLD
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from src.services.json_service import load_json, save_json

class ModelService:
    _instance = None

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def _embed_text(self, text: str) -> list:
        return self.model.encode(text).tolist()

    def embed_file(self, label: str, text: str):
        embedding = self._embed_text(text)
        embedding_db = load_json(EMBEDDINGS_FILE)

        embedding_db[label] = embedding
        save_json(EMBEDDINGS_FILE, embedding_db)

    def classify_file(self, text: str): #old
        """
        Classifies the file using its content.
        """
        file_embedding = self._embed_text(text)

        embedding_db = load_json(EMBEDDINGS_FILE)
        if not embedding_db:
            raise FileNotFoundError("No embeddings found. Please register file types first.")

        similarities = {
            label: cosine_similarity([file_embedding], [np.array(vec)])[0][0]
            for label, vec in embedding_db.items()
        }

        best_match = max(similarities.items(), key=lambda x: x[1])
        return best_match[0] if best_match[1] >= SIMILARITY_THRESHOLD else "unknown"