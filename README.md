# Tailor4Job

Tailor4Job is a command-line tool that helps candidates tailor their resume and cover letter to specific job descriptions. By leveraging the Groq API and a specified model, Tailor4Job analyzes your resume and cover letter in relation to a job description, providing valuable insights to optimize your application for better chances of passing Applicant Tracking System (ATS) screenings.

## Features
- **Resume and Cover Letter Analysis**: Compare your resume and cover letter with the job description to highlight relevant skills and experiences.
- **Detailed Feedback**: Receive in-depth insights into your strengths, areas for improvement, and specific recommendations.
- **ATS Compatibility Analysis**: Get an estimation of your application's compatibility with ATS, including keyword suggestions.
- **Customizable Models**: Use different processing models (e.g., `llama3-8b-8192`) for analysis. [Optional Feature]
- **Flexible File Formats**: Choose between `.docx` or `.pdf` output formats for tailored documents. [Optional Feature]

## Installation

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

## Usage

### Basic Analysis Command
To perform a basic analysis, run:
```bash
python main.py --model llama3-8b-8192 --output Output_Analysis.docx --analysis_mode basic GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt
```

### Detailed Analysis Command
For a more comprehensive analysis:
```bash
python main.py --model llama3-8b-8192 --output Output_Analysis.docx --analysis_mode detailed GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt
```

### Display Version
To check the current version of Tailor4Job:
```bash
python main.py --version
```

### Display Help
To see all available options:
```bash
python main.py --help
```

### Command-Line Options
- **`--model` or `-m`**: Specify the AI model for processing (default: `llama3-8b-8192`).
  ```bash
  python main.py --model custom-model file1.docx
  ```

- **`--output` or `-o`**: Specify the filename for the output (supports `.docx` and `.pdf`).
  ```bash
  python main.py --output tailored_resume.docx file1.docx
  ```

- **`--analysis_mode` or `-a`**: Choose analysis type (`basic` or `detailed`).

## Inputs and Outputs

### Input Files
- **Resume**: A `.docx` file with your general resume.
- **Cover Letter**: A `.docx` file with your general cover letter.
- **Job Description**: A `.txt` file containing the job description.

### Output
Tailored resume and cover letter analysis results are saved as either `.docx` or `.pdf` files based on your preference.

## Example Commands

### Basic Analysis Example (in `.docx` format):
```bash
python main.py --analysis_mode basic --output basic_analysis_output.docx GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt
```

### Detailed Analysis Example (in `.pdf` format):
```bash
python main.py --analysis_mode detailed --output detailed_analysis_output.pdf GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy tailoring, and best of luck with your job applications!
```