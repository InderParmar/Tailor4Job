import os
from click.testing import CliRunner
from main import main
from docx import Document

def create_docx(file_path, content):
    doc = Document()
    doc.add_paragraph(content)
    doc.save(file_path)

def test_main_arg_parsing():
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
            "--analysis_mode", "detailed",
            "resume.docx", "cover_letter.docx", "job_description.txt"
        ])
        
        print(result.output)  # Print output for debugging
        assert result.exit_code == 0
    finally:
        # Clean up temporary files
        os.remove("resume.docx")
        os.remove("cover_letter.docx")
        os.remove("job_description.txt")
