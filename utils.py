import os
from groq import Groq
from docx import Document
import pdfkit


def process_files(files, api_key, model, mode):
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
    if mode == 'detailed':
        prompt = """
    Attached are the Resume, Cover Letter, and Job Description for which the candidate is applying for the job.

    What I want from you is to analyze the Resume and Cover Letter and compare them to the Job Description.

    1. **Brief Introduction**:
       - Introduce the job and the candidate (mention the name of the candidate from the Resume).

    2. **Analysis Results**:
       - Compare the Resume to the Job Description:
         - Is the candidate a good fit or not?
         - What are the candidate's strong points for this job?
         - What are the candidate's weaknesses?
         - How can the candidate improve the Resume?
        - What are the candidate's major mistakes that are being made while formatting the Resume? If there are any major mistakes, mention them here, 
            otherwise just ignore this section and jumpt to the Next section.
       - Compare the Cover Letter to the Job Description:
         - Is the cover letter aligned with the job requirements?
         - What improvements can be made?
         - What are the candidate's major mistakes that are being made while formatting the Cover Letter? If there are any major mistakes, mention them here, 
            otherwise just ignore this section and jumpt to the next section.

    3. **Summary**:
       - Estimate the percentage chance that this Resume and Cover Letter can pass the ATS system for this job. Answer this point in terms of percentage
       - List any important keywords that can be added to the Resume and Cover Letter.
       - Suggest keywords that should be replaced with better alternatives.

    Make sure each section is clearly labeled as mentioned above and structured as described.
    """
    else:
        prompt = """
        Attached are the Resume, Cover Letter, and Job Description for which the candidate is applying for the job.

        Please provide:
        1. A brief introduction to the job and candidate.
        2. An estimated percentage chance of the resume and cover letter passing an ATS system.
        """
    full_content = prompt + "\n\n" + content
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
