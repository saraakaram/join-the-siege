# Heron File Classifier

This project is a real-world challenge to improve and productionize a file classification service. The goal is to build a scalable, maintainable, and intelligent system that can classify poorly named documents by analyzing their content, support new file types, and be ready for deployment.

---

## Features

- Semantic classification using [Sentence-BERT](https://www.sbert.net/)
- Supports PDF, Word, Excel, JPG, PNG
- Dynamic addition of new file classes
- Unit and integration tests for endpoints
- Dockerized for production

---

## Project Structure

```

join-the-siege/
│
├── src/
│   ├── app.py                 # Flask app entrypoint
│   ├── config.py              # Constants and paths
│   ├── controllers/           # Route definitions
│   ├── services/              # Business logic (file processing, model, JSON)
│   ├── assets/embeddings/     # Embedding store (JSON)
│   └── exceptions/            # Custom exceptions
│
├── files/                     # Sample files for testing
├── tests/                     # Pytest test suite
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions for CI/CD
├── requirements.txt
├── Dockerfile
└── README.md

````

---

## Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/saraakaram/heron-classifier.git
cd heron-classifier
````

### 2. Install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Run the App (Dev Mode)

```bash
python src/app.py
```

Server runs at `http://localhost:5000`

---

## Run Tests

```bash
pytest
```

---

## Docker

### Build image

```bash
docker build -t heron-classifier .
```

### Run container

```bash
docker run -p 5000:5000 heron-classifier
```

---

## API Endpoints

### `POST /classify_file`

Classifies an uploaded file.

**Body (multipart/form-data):**

* `file`: document (PDF, Word, Excel, JPG, PNG)

**Response:**

```json
{ "file_class": "invoice" }
```

---

### `POST /add_class`

Registers a new file type by providing a sample document.

**Body (multipart/form-data):**

* `file_type`: string (e.g., "tax\_document")
* `file`: sample file for that type

**Response:**

```json
{ "message": "File type 'tax_document' registered successfully." }
```

---

### `GET /health`

Simple health check.

```json
{ "status": "OK" }
```

---

## Notes

* Reference embeddings are stored in: `src/assets/embeddings/embeddings.json`
* For detailed explanation of the classification strategy and codebase structure, please refer to Solution_Overview.pdf

---

## Author

Built with ❤️ by Sara Karam for Heron Data
GitHub: [@saraakaram](https://github.com/saraakaram)

---