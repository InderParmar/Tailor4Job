import pytest
from utils import generate_output
import os

DOCX_PATH = "nested/directory/test_output.docx"
PDF_PATH = "nested/directory/test_output.pdf"

@pytest.fixture(autouse=True)
def cleanup():
    yield
    for path in [DOCX_PATH, PDF_PATH]:
        if os.path.exists(path):
            os.remove(path)

def test_generate_output_with_nested_path_docx():
    content = "Testing nested directory path for .docx"
    os.makedirs(os.path.dirname(DOCX_PATH), exist_ok=True)
    generate_output(content, DOCX_PATH)
    assert os.path.exists(DOCX_PATH)

def test_generate_output_with_nested_path_pdf():
    content = "Testing nested directory path for .pdf"
    os.makedirs(os.path.dirname(PDF_PATH), exist_ok=True)
    generate_output(content, PDF_PATH)
    assert os.path.exists(PDF_PATH)
