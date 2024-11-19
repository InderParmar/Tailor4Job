import sys
import os
from click.testing import CliRunner
from main import main
from docx import Document

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

CUSTOM_OUTPUT_DOCX = "llama3-8b-8192_custom_output_analysis.docx"

def create_docx(file_path, content):
    doc = Document()
    doc.add_paragraph(content)
    doc.save(file_path)

def test_custom_output_filename():
    # Create temporary DOCX files with valid structure
    create_docx("resume.docx", "Sample resume content.")
    create_docx("cover_letter.docx", "Sample cover letter content.")
    
    # Create a simple text file for the job description
    with open("job_description.txt", "w") as f:
        f.write("Sample job description content.")
    
    try:
        # Run the CLI command
        runner = CliRunner()
        result = runner.invoke(main, [
            "--model", "llama3-8b-8192",
            "--provider", "groq",
            "--output", "custom_output_analysis.docx",
            "--analysis_mode", "detailed",
            "resume.docx", "cover_letter.docx", "job_description.txt"
        ])
        
        print(result.output)  # Print output for debugging
        assert result.exit_code == 0
        assert os.path.exists(CUSTOM_OUTPUT_DOCX), "Custom output file was not created."
    finally:
        # Clean up temporary files
        os.remove("resume.docx")
        os.remove("cover_letter.docx")
        os.remove("job_description.txt")
        if os.path.exists(CUSTOM_OUTPUT_DOCX):
            os.remove(CUSTOM_OUTPUT_DOCX)
