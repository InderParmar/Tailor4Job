import sys
import os
from unittest.mock import patch, MagicMock
from utils import process_files
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Define a sample response for mocking
sample_response_content = "This is a sample response from Groq API."
sample_response_usage = {
    "prompt_tokens": 10,
    "completion_tokens": 20,
    "total_tokens": 30
}

def test_groq_api_response():
    # Define test parameters
    files = ["resume.docx", "cover_letter.docx", "job_description.txt"]
    api_key = "test_key"
    model = "llama3-8b-8192"
    mode = "detailed"
    provider_name = "groq"

    # Mock file contents for .docx and .txt files
    with patch("utils.Document") as mock_document, patch("builtins.open", new_callable=MagicMock) as mock_open, \
         patch("utils.Groq") as mock_groq_client:
        # Mock .docx content
        mock_document.return_value.paragraphs = [type("Paragraph", (object,), {"text": "Sample content"})()]
        # Mock .txt content
        mock_open.return_value.__enter__.return_value.read.return_value = "Sample job description content."

        # Mock Groq API response
        mock_groq_instance = mock_groq_client.return_value
        mock_groq_instance.chat.completions.create.return_value.choices[0].message.content = sample_response_content
        mock_groq_instance.chat.completions.create.return_value.usage = sample_response_usage

        # Run the function
        result_content, token_info = process_files(files, api_key, model, mode, True, provider_name)

        # Assertions to verify the mocked API response
        assert result_content == sample_response_content
        assert token_info["prompt_tokens"] == 10
        assert token_info["completion_tokens"] == 20
        assert token_info["total_tokens"] == 30
