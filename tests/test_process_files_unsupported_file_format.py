import pytest
from utils import process_files
 
def test_process_files_unsupported_file_format():
    files = ["unsupported_file_format.pdf"]  # Unsupported format for process_files
    api_key = "test_key"
    model = "llama3-8b-8192"
    mode = "detailed"
    provider_name = "groq"
 
    with pytest.raises(Exception, match="Unsupported file format"):
        process_files(files, api_key, model, mode, token_usage=True, provider_name=provider_name)