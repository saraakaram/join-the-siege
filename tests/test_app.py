from io import BytesIO
import pytest
from src.app import create_app
from src.services.file_service import get_file_extension, is_valid
from pathlib import Path

FILES_DIR = Path(__file__).resolve().parent.parent / "files"

@pytest.fixture
def client():
    app = create_app() 
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# CLASSIFY ENDPOINT TEST #
@pytest.mark.parametrize("filename, expected", [
    ("file.pdf", True),
    ("file.png", True),
    ("file.jpg", True),
    ("file.txt", False),
    ("file", False),
])
def test_allowed_file(filename, expected):
    assert is_valid(get_file_extension(filename)) == expected

def test_no_file_in_request(client):
    response = client.post('/classify_file')
    assert response.status_code == 400

def test_no_selected_file(client):
    data = {'file': (BytesIO(b""), '')}  # Empty filename
    response = client.post('/classify_file', data=data, content_type='multipart/form-data')
    assert response.status_code == 400

@pytest.mark.parametrize("filename, expected_class", [
    ("bank_statement_2.pdf", "bank_statement"),
    ("drivers_licence_2.jpg", "drivers_license"),
    ("invoice_2.pdf", "invoice"),
    ("tax_document_1.pdf", "unknown"),  # Tax document is not added as a class yet
])
def test_real_file_classification(client, filename, expected_class):
    filepath = FILES_DIR / filename
    assert filepath.exists(), f"File not found: {filepath}"

    with open(filepath, "rb") as f:
        data = {'file': (f, filename)}
        response = client.post("/classify_file", data=data, content_type="multipart/form-data")

    assert response.status_code == 200
    result = response.get_json()["file_class"]

    assert result == expected_class, f"{filename} classified as {result}, expected {expected_class}"

# ADD FILE TYPE TEST #
def test_add_class_missing_fields(client):
    response = client.post('/add_class', data={})
    assert response.status_code == 400

def test_add_tax_document_success(client):
    """
    This version uses a real sample file: files/tax_document_1.pdf
    """
    filepath = FILES_DIR / "tax_document_1.pdf"
    assert filepath.exists(), f"Missing file: {filepath}"

    with open(filepath, "rb") as f:
        data = {
            'file_type': 'tax_document',
            'file': (f, filepath.name)
        }
        response = client.post('/add_class', data=data, content_type='multipart/form-data')

    assert response.status_code == 200
    assert "registered successfully" in response.get_json()["message"]

# CLASSIFY NEW TAX DOCUMENT now that it's a registered class #
def test_classify_tax_document(client):
    """
    Sends a real tax document PDF and expects it to be classified as 'tax_document'
    """
    filepath = FILES_DIR / "tax_document_2.jpg"
    assert filepath.exists(), f"Missing test file: {filepath}"

    with open(filepath, "rb") as f:
        data = {
            'file': (f, filepath.name)
        }
        response = client.post("/classify_file", data=data, content_type="multipart/form-data")

    assert response.status_code == 200
    result = response.get_json()["file_class"]

    assert result == "tax_document", f"Expected 'tax_document', got '{result}'"

# HEALTH CHECK TEST #

def test_health_check(client):
    response = client.get('/health_check')
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}