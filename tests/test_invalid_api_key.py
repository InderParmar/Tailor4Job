import pytest
from unittest.mock import patch, MagicMock
from utils import process_files

def test_invalid_api_key():
    files = ["test_resume.docx", "test_cover_letter.docx", "job_description.txt"]
    invalid_api_key = "invalid_key"
    
    with patch("utils.Document") as mock_document:
        # Mock Document to avoid file access for .docx files
        mock_document.return_value = MagicMock()
        
        with patch("builtins.open", new_callable=MagicMock) as mock_open:
            # Mock open to avoid file access for text files
            mock_open.return_value.__enter__.return_value.read.return_value = "Sample content"
            
            with patch("utils.requests.post") as mock_post:
                mock_post.return_value.status_code = 401  # Unauthorized
                mock_post.return_value.json.return_value = {"error": {"message": "Invalid API Key"}}
                
                with pytest.raises(Exception, match="Invalid API Key"):
                    process_files(files, invalid_api_key, model="llama3-8b-8192", mode="detailed", token_usage=True, provider_name="groq")
