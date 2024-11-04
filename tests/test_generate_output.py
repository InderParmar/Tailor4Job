import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import generate_output

import pytest
import os

# Temporary output files for testing
DOCX_OUTPUT_FILE = "test_output.docx"
PDF_OUTPUT_FILE = "test_output.pdf"
UNSUPPORTED_OUTPUT_FILE = "test_output.txt"

@pytest.fixture(autouse=True)
def cleanup():
    # Cleanup after each test
    yield
    for file in [DOCX_OUTPUT_FILE, PDF_OUTPUT_FILE, UNSUPPORTED_OUTPUT_FILE]:
        if os.path.exists(file):
            os.remove(file)

def test_generate_docx_output():
    """
    Test case for generating a valid .docx file.
    """
    content = "This is a test content for docx file."
    generate_output(content, DOCX_OUTPUT_FILE)
    
    # Check if file was created
    assert os.path.exists(DOCX_OUTPUT_FILE), "DOCX file was not created."
    assert os.path.getsize(DOCX_OUTPUT_FILE) > 0, "DOCX file is empty."

def test_generate_pdf_output():
    """
    Test case for generating a valid .pdf file.
    """
    content = "This is a test content for pdf file."
    generate_output(content, PDF_OUTPUT_FILE)
    
    # Check if file was created
    assert os.path.exists(PDF_OUTPUT_FILE), "PDF file was not created."
    assert os.path.getsize(PDF_OUTPUT_FILE) > 0, "PDF file is empty."

def test_unsupported_file_format():
    """
    Test case for handling unsupported file formats.
    """
    content = "This is a test content for unsupported file."
    
    # Expect an exception for unsupported file formats
    with pytest.raises(Exception, match="Unsupported file format"):
        generate_output(content, UNSUPPORTED_OUTPUT_FILE)

def test_empty_content_docx():
    """
    Test case for handling empty content for .docx output.
    """
    content = ""
    generate_output(content, DOCX_OUTPUT_FILE)
    
    # Check if file was created
    assert os.path.exists(DOCX_OUTPUT_FILE), "DOCX file was not created."
    # Verify that the file size is not excessively large for empty content
    assert os.path.getsize(DOCX_OUTPUT_FILE) < 50000, "DOCX file is unexpectedly large for empty content."

def test_empty_content_pdf():
    """
    Test case for handling empty content for .pdf output.
    """
    content = ""
    generate_output(content, PDF_OUTPUT_FILE)
    
    # Check if file was created
    assert os.path.exists(PDF_OUTPUT_FILE), "PDF file was not created."
    # Verify that the file size is not excessively large for empty content
    assert os.path.getsize(PDF_OUTPUT_FILE) < 5000, "PDF file is unexpectedly large for empty content."

def test_null_content_docx():
    """
    Test case for handling None as content for .docx output.
    """
    with pytest.raises(TypeError, match="Content must be a string, not NoneType."):
        generate_output(None, DOCX_OUTPUT_FILE)

def test_null_content_pdf():
    """
    Test case for handling None as content for .pdf output.
    """
    with pytest.raises(TypeError, match="Content must be a string, not NoneType."):
        generate_output(None, PDF_OUTPUT_FILE)
