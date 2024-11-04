# Contributing to Tailor4Job

Thank you for considering contributing to Tailor4Job! This guide will help you set up the development environment, understand the structure of the project, and use tools like formatters and linters to maintain code quality.

## Table of Contents
- [Getting Started](#getting-started)
- [Setting Up the Development Environment](#setting-up-the-development-environment)
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

### Setting Up the Development Environment

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

### Source Code Formatting

We use **Ruff** as our automatic code formatter to ensure consistent code style across the project.

1. **Install Ruff** (if not already installed):
   ```bash
   pip install ruff
   ```

2. **Run the Formatter**:
   - To format the entire codebase, use the provided `format.sh` script:
     ```bash
     ./format.sh
     ```
   - This script will automatically format all Python files in the project.

3. **Configuration**:
   - The configuration file `.ruff.toml` contains the formatting rules for Ruff.
   - Files and directories that should not be formatted (like `env` or `__pycache__`) are specified in this file.

### Linting

Ruff is also used as a linter to check for common issues and enforce best practices.

1. **Run the Linter**:
   - You can run Ruff as a linter by executing:
     ```bash
     ruff .
     ```
   - Fix any warnings or errors identified by Ruff to maintain code quality.

2. **Ignoring Specific Lines or Files**:
   - Sometimes, specific lines of code may need to be ignored by the linter. You can do this by adding a `# noqa` comment at the end of the line.

3. **Documentation**:
   - Instructions for using Ruff are included in this document for contributors who are unfamiliar with it.

### Editor/IDE Integration

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

2. **Other Editors**:
   - Consult Ruff’s documentation to configure it in your preferred editor.

### Running Tests

To ensure your changes work as expected, run tests after making modifications.

```bash
# Example test command (update with actual test framework if applicable)
python -m unittest discover
```

### Git Workflow

1. **Create a Branch**:
   - Create a new branch for your changes:
     ```bash
     git checkout -b your-feature-branch
     ```

2. **Commit Regularly**:
   - Make small, frequent commits with clear messages:
     ```bash
     git commit -m "Add feature X"
     ```

3. **Squash Commits**:
   - Before merging, squash commits into a single commit:
     ```bash
     git rebase -i HEAD~[number_of_commits]
     ```

4. **Push and Open a Pull Request**:
   - Push your branch to GitHub:
     ```bash
     git push origin your-feature-branch
     ```
   - Open a pull request with a description of your changes.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping improve Tailor4Job!
```