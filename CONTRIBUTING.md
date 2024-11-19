# Contributing to Tailor4Job

Thank you for considering contributing to Tailor4Job! This guide will help you set up the development environment, understand the structure of the project, and use tools like formatters, linters, and testing frameworks to maintain code quality.

## Table of Contents
- [Getting Started](#getting-started)
- [Setting Up the Development Environment](#setting-up-the-development-environment)
- [Continuous Integration (CI)](#continuous-integration-ci)
- [Source Code Formatting](#source-code-formatting)
- [Linting](#linting)
- [Editor/IDE Integration](#editoride-integration)
- [Running Tests](#running-tests)
- [Git Workflow](#git-workflow)

---

## Getting Started

To start contributing, fork the repository and clone your forked version:

```bash
git clone https://github.com/your-username/Tailor4Job
cd Tailor4Job
```

---

## Setting Up the Development Environment

1. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory and add your API key:
     ```bash
     GROQ_API_KEY=your_actual_api_key_here
     ```

---

## Continuous Integration (CI)

We have integrated **GitHub Actions** to automate the testing process whenever changes are pushed to the repository. The workflow file (`.github/workflows/python-app.yml`) ensures that:

1. All Python dependencies are installed.
2. `pytest` is run to verify that all tests pass.
3. External dependencies like `wkhtmltopdf` are installed for PDF generation tests.

### Triggering the CI Pipeline
The CI pipeline is triggered:
- Automatically when you push changes to the `main` branch.
- When a pull request is created or updated.

If you're adding new tests, ensure they pass locally before pushing to avoid CI failures.

---

## Source Code Formatting

We use **Ruff** as our automatic code formatter to ensure consistent code style across the project.

1. **Install Ruff** (if not already installed):
   ```bash
   pip install ruff
   ```

2. **Run the Formatter**:
   - To format the entire codebase:
     ```bash
     ruff check . --fix
     ```

3. **Configuration**:
   - Ruff settings are stored in `.ruff.toml`.

---

## Linting

Ruff is also used as a linter to check for common issues and enforce best practices.

1. **Run the Linter**:
   ```bash
   ruff check .
   ```

2. **Ignoring Specific Lines or Files**:
   - Use `# noqa` at the end of a line to ignore specific linting errors.

---

## Editor/IDE Integration

For an efficient development experience, integrate Ruff with your editor to automatically format and lint code on save.

1. **VS Code Integration**:
   - Install the Ruff extension for VS Code.
   - Add a `.vscode/settings.json` file to the project with the following configuration:
     ```json
     {
       "python.formatting.provider": "ruff",
       "editor.formatOnSave": true,
       "python.linting.ruffEnabled": true
     }
     ```

---

## Running Tests

We use **pytest** as our testing framework, with **requests-mock** for mocking external API calls. 

### **Steps to Run Tests**
1. **Install Testing Dependencies**:
   ```bash
   pip install pytest requests-mock
   ```

2. **Run All Tests**:
   ```bash
   pytest
   ```

3. **Run a Specific Test**:
   ```bash
   pytest path/to/test_file.py
   ```

### **Using Continuous Integration for Tests**
- The GitHub Actions CI workflow automatically runs `pytest` on every push or pull request.
- External dependencies like `wkhtmltopdf` are installed in the CI environment to support PDF-related tests.

### **Mocking API Calls**
Tests that involve external API calls are mocked using `requests-mock` to avoid relying on live services. This ensures tests are reliable and consistent.

---

## Git Workflow

1. **Create a Branch**:
   ```bash
   git checkout -b your-feature-branch
   ```

2. **Commit Regularly**:
   ```bash
   git commit -m "Add feature X"
   ```

3. **Push Changes**:
   ```bash
   git push origin your-feature-branch
   ```

4. **Open a Pull Request**:
   - Open a pull request from your branch to `main`.

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

### Thank you for helping improve Tailor4Job!

This updated guide includes the new CI setup and how contributors can use it effectively.