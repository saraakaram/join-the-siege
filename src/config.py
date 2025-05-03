from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
EMBEDDINGS_FILE = BASE_DIR / "src" / "assets" / "embeddings" / "embeddings.json"

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'docx', 'xlsx'}
SIMILARITY_THRESHOLD = 0.4