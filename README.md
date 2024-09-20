# Tailor4Job

Tailor4Job is a command-line tool that helps candidates tailor their resume and cover letter to specific job descriptions. Using the Groq API and a specified model, this tool compares the resume and cover letter to the job description and provides a detailed analysis of the candidate's fit for the job. Additionally, it gives suggestions for improvements, analyzes keywords for ATS (Applicant Tracking System) compatibility, and offers recommendations to improve the chances of passing automated screening systems.

## Features
- **Resume and Cover Letter Analysis**: Compare the resume and cover letter against the job description.
- **Detailed Feedback**: Provides insights into the candidate’s strengths, weaknesses, and suggestions for improvement.
- **ATS Compatibility Analysis**: Estimates the chances of the resume and cover letter passing an ATS system and offers keyword suggestions.
- **Modes**: Choose between a basic or detailed analysis. [ Optional Feature ] 
- **Supports Multiple Files**: Accepts multiple input files such as resume, cover letter, and job description. [ Optional Feature ]
- **Custom Model Support**: Specify the model to use for processing (e.g., `llama3-8b-8192`).  [ Optional Feature ]
- **Custom Output File Format Support**: Specify the output file format, two options are provided i.e. .pdf and .docx . [ Optional Feature ]

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/InderParmar/Tailor4Job
   cd Tailor4Job

2. **Create and Activate Virtual Environment (Optional but Recommended)**:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the required Python packages listed in the `requirements.txt` file (if available), or manually install the necessary packages:
   ```bash
   pip install click python-dotenv python-docx pdfkit groq
   ```

4. **Set Up `wkhtmltopdf`** (if you plan to generate PDF outputs):
   - Download and install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html), ensuring it is available in your system's PATH.

5. **Configure the `.env` File**:
   - Create a `.env` file in the root directory and add your Groq API key:
     ```bash
     GROQ_API_KEY=your_actual_api_key_here
     ```

## Usage

### Basic Command
To run the tool with basic analysis:
```bash
python main.py --model llama3-8b-8192 --output Output_Analysis.docx --analysis_mode basic GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt
```

### Detailed Analysis Command
To run the tool with a detailed analysis:
```bash
python main.py --model llama3-8b-8192 --output Output_Analysis.docx --analysis_mode detailed GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt
```

### Display Version
To check the version of the tool:
```bash
python main.py --version
```

### Inputs:
- **Resume**: A `.docx` file containing the candidate's general resume.
- **Cover Letter**: A `.docx` file containing the candidate's general cover letter.
- **Job Description**: A `.txt` file with the job description.

### Outputs:
- The tailored resume and cover letter can be saved as `.docx` or `.pdf` files.
- Example output will be added below.

## Features and Options

### `--model` or `-m`
Specify the AI model to use for processing. The default is `llama3-8b-8192`.
```bash
python main.py --model custom-model file1.docx
```

### `--output` or `-o`
Specify the filename to save the output. If this option is not provided, the output will be printed to the terminal.
```bash
python main.py --output tailored_resume.docx file1.docx
```

### `--analysis-mode` or `-a`
Choose between `basic` and `detailed` analysis modes.
- `basic`: Provides a high-level analysis.
- `detailed`: Offers a more thorough comparison with suggestions for improvements.

### Error and Debugging Information
All debug information, such as the progress of file processing and errors, will be printed to `stderr` to avoid mixing it with normal output.

## Debugging Information

To capture error or debug information (which is written to `stderr`), use the following command to separate it from normal output:

```bash
python main.py --model llama3-8b-8192 --output tailored_resume.docx GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt 2>error.log
```

This will log error and debug information into `error.log` while the normal output will go to `tailored_resume.docx`.

## Sample Inputs

To use the Tailor4Job tool effectively, you will need to provide three types of input files:

1. **Resume (Word Document - `.docx`)**:
   - This should be a general resume in a `.docx` format.
   - The resume will be compared against the job description to evaluate the candidate's strengths and weaknesses in relation to the job.
   
   Example: `GENERAL_RESUME.docx`

2. **Cover Letter (Word Document - `.docx`)**:
   - This is the candidate's cover letter in `.docx` format.
   - The cover letter will also be analyzed to assess how well it aligns with the job description and what improvements can be made.
   
   Example: `General_Cover_Letter.docx`

3. **Job Description (Text File - `.txt`)**:
   - This file should contain the job description for the position the candidate is applying for.
   - The tool will use the job description to compare the resume and cover letter, identifying areas where the candidate matches well and where they need improvement.
   
   Example: `job_description.txt`

### Input Format Guidelines

- The **resume** and **cover letter** must be in the `.docx` format to be processed correctly.
- The **job description** should be in a `.txt` file, containing plain text outlining the job responsibilities, qualifications, and any important keywords the employer is looking for.
  
### Example Usage with Sample Inputs

```bash
python main.py --model llama3-8b-8192 --output tailored_resume.docx --analysis-mode detailed GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt

## Example Commands

#### Basic Analysis Example in docx format:
```bash
python main.py --analysis_mode basic --output basic_analysis_output.docx GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt
```
#### Here are examples of the Basic Analysis generated by Tailor4Job in docx format:

- [Download Basic Analysis Example (Word Document)](./Examples/OUTPUT/DOCS_OUTPUT/basic_analysis_output.docx)

#### Detailed Analysis Example in docx format:
```bash
python main.py --analysis_mode detailed --output detailed_analysis_output.docx GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt
```
#### Here are examples of the Detailed Analysis generated by Tailor4Job in docx format:

- [Download Detailed Analysis Example (Word Document)](./Examples/OUTPUT/DOCS_OUTPUT/detailed_analysis_output.docx)
  
#### Basic Analysis Example in pdf format:
```bash
python main.py --analysis_mode basic --output basic_analysis_output.pdf GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt
```
#### Here are examples of the Basic Analysis generated by Tailor4Job in docx format:

- [Download Basic Analysis Example (PDF Document)](./Examples/OUTPUT/PDF_OUTPUT/basic_analysis_output.pdf)

#### Detailed Analysis Example in pdf format:
```bash
python main.py --analysis_mode detailed --output detailed_analysis_output.pdf GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt
```
#### Here are examples of the Detailed Analysis generated by Tailor4Job in docx format:

- [Download Detailed Analysis Example (PDF Document)](./Examples/OUTPUT/PDF_OUTPUT/detailed_analysis_output.pdf)
  
#### Viewing Output:
Output can be written to a file or printed in the terminal. For example, to print the output to the terminal instead of saving it to a file:
```bash
python main.py GENERAL_RESUME.docx General_Cover_Letter.docx job_description.txt
```
- [Download Example of Viewing Analysis on the Terminal](./Examples/OUTPUT/Terminal_Output/Screenshot_2024-09-20_5.15.10_PM.png)


## Contribution

Feel free to fork the repository and submit pull requests. Contributions are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
