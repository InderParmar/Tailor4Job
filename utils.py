import os
from groq import Groq
from docx import Document
import pdfkit


def process_files(files, api_key, model):
    """
    Process input files using the Groq SDK and return the tailored content.
    """
    # Initialize the Groq client
    client = Groq(api_key=api_key)

    # Read content from input files
    content = ''
    for file_path in files:
        if file_path.endswith('.docx'):
            # Read .docx file content
            doc = Document(file_path)
            for para in doc.paragraphs:
                content += para.text + '\n'
        else:
            # Read other files assuming they are text-based
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                content += file.read() + '\n'

    # Call the Groq API to process the content
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model=model,
    )

    tailored_content = response.choices[0].message.content
    return tailored_content


def generate_output(content, output_file):
    """
    Generate output file in either .docx or .pdf format.
    """
    if output_file.endswith('.docx'):
        generate_docx(content, output_file)
    elif output_file.endswith('.pdf'):
        generate_pdf(content, output_file)
    else:
        raise Exception('Unsupported file format. Please use .docx or .pdf.')

def generate_docx(content, output_file):
    """
    Generate a .docx file with the given content.
    """
    doc = Document()
    doc.add_paragraph(content)
    doc.save(output_file)

def generate_pdf(content, output_file):
    """
    Generate a .pdf file with the given content.
    """
    # Create a temporary HTML file to convert to PDF
    html_content = f'<html><body><p>{content}</p></body></html>'
    pdfkit.from_string(html_content, output_file)
