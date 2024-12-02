# Tailor4Job

Tailor4Job is a command-line tool that helps candidates tailor their resume and cover letter to specific job descriptions. By leveraging the Groq API and a specified model, Tailor4Job analyzes your resume and cover letter in relation to a job description, providing valuable insights to optimize your application for better chances of passing Applicant Tracking System (ATS) screenings.

---

## Features
- **Resume and Cover Letter Analysis**: Compare your resume and cover letter with the job description to highlight relevant skills and experiences.
- **Detailed Feedback**: Receive in-depth insights into your strengths, areas for improvement, and specific recommendations.
- **ATS Compatibility Analysis**: Get an estimation of your application's compatibility with ATS, including keyword suggestions.
- **Customizable Models**: Use different processing models (e.g., `llama3-8b-8192`) for analysis. [Optional Feature]
- **Flexible File Formats**: Choose between `.docx` or `.pdf` output formats for tailored documents. [Optional Feature]

---

## Prerequisites
Ensure the following are installed on your system:
1. **Python 3.7 or later**: [Download Python](https://www.python.org/downloads/)
   - Check if Python is installed:
     ```bash
     python --version
     ```
   - Ensure pip (Python package manager) is installed:
     ```bash
     pip --version
     ```
2. **wkhtmltopdf**: Required for PDF generation.
   - [Download and Install wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)
   - Verify installation:
     ```bash
     wkhtmltopdf --version
     ```
3. **Groq API Key**:
   - You must sign up for the [Groq API](https://groq.com) to obtain your API key (details in the [Get an API Key](#get-an-api-key) section).

---

## Installation

### Option 1: From npm (Recommended)
1. Install Tailor4Job globally using npm:
   ```bash
   npm install -g tailor4job
   ```
2. Test the installation:
   ```bash
   tailor4job --help
   ```

---

### Option 2: From Source
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/InderParmar/Tailor4Job
   cd Tailor4Job
   ```

2. **Create and Activate a Virtual Environment** (recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up `wkhtmltopdf`** (for PDF output):
   - Download and install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) and ensure it’s available in your system’s PATH.

5. **Configure the `.env` File**:
   - Create a `.env` file in the project root and add your Groq API key:
     ```bash
     GROQ_API_KEY=your_actual_api_key_here
     ```

---

## Usage

### Tailor4Job Commands
Run Tailor4Job from the command line to analyze your resume and cover letter.

#### Basic Analysis Command
```bash
tailor4job --model llama3-8b-8192 --output Output_Analysis.docx --analysis_mode basic GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt
```

#### Detailed Analysis Command
```bash
tailor4job --model llama3-8b-8192 --output Output_Analysis.docx --analysis_mode detailed GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt
```

#### Check Version
```bash
tailor4job --version
```

#### Display Help
```bash
tailor4job --help
```

---

## Get an API Key
To use Tailor4Job, you’ll need an API key for the Groq API. Follow these steps:

1. **Sign up** for an account at [Groq API](https://groq.com).
2. Navigate to the API section and **generate an API key**.
3. Add the API key to your `.env` file in the project root:
   ```bash
   GROQ_API_KEY=your_actual_api_key_here
   ```

---

## Troubleshooting

1. **Python Not Found**:
   - Ensure Python is installed and added to your system’s PATH.
   - For Windows, re-install Python and select the "Add Python to PATH" option during setup.

2. **pip Command Not Recognized**:
   - Ensure pip is installed. Use the following command to install pip manually:
     ```bash
     python -m ensurepip --upgrade
     ```

3. **wkhtmltopdf Not Found**:
   - Verify wkhtmltopdf is installed and added to PATH:
     ```bash
     wkhtmltopdf --version
     ```

4. **Command Not Found After npm Installation**:
   - Ensure npm's global bin directory is in your PATH:
     ```bash
     npm config get prefix
     ```
     Add `/prefix/bin` to your PATH if necessary.

5. **API Key Missing**:
   - Ensure the `.env` file contains the correct API key. The tool will raise an error if the key is missing or invalid.

---

## Inputs and Outputs

### Input Files
- **Resume**: A `.docx` file with your general resume.
- **Cover Letter**: A `.docx` file with your general cover letter.
- **Job Description**: A `.txt` file containing the job description.

### Output
Tailored resume and cover letter analysis results are saved as either `.docx` or `.pdf` files based on your preference.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy tailoring, and best of luck with your job applications! 🚀
