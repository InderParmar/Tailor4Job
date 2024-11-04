from click.testing import CliRunner
from main import main

def test_invalid_file_input():
    runner = CliRunner()
    result = runner.invoke(main, [
        "--model", "llama3-8b-8192",
        "--provider", "groq",
        "--analysis_mode", "detailed",
        "nonexistent_resume.docx", "nonexistent_cover_letter.docx", "nonexistent_job_description.txt"
    ])
    
    assert result.exit_code != 0
    assert "Invalid value for '[FILES]...': Path 'nonexistent_resume.docx' does not exist." in result.output
