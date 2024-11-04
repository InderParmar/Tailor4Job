import os
import pytest
from utils import generate_output

LARGE_DOCX = "large_test_output.docx"
LARGE_PDF = "large_test_output.pdf"

@pytest.fixture(autouse=True)
def cleanup():
    yield
    for file in [LARGE_DOCX, LARGE_PDF]:
        if os.path.exists(file):
            os.remove(file)

def test_generate_large_content_docx():
    large_content = "This is a large content. " * 10000
    generate_output(large_content, LARGE_DOCX)
    assert os.path.exists(LARGE_DOCX)
    assert os.path.getsize(LARGE_DOCX) > 0

def test_generate_large_content_pdf():
    large_content = "This is a large content. " * 10000
    generate_output(large_content, LARGE_PDF)
    assert os.path.exists(LARGE_PDF)
    assert os.path.getsize(LARGE_PDF) > 0
