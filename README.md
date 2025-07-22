# Code Explainer Project

## Overview
The Code Explainer project is a Visual Studio Code extension that leverages a language model to analyze and explain code snippets. It provides a user-friendly interface for developers to gain insights into their code, enhancing understanding and productivity.

## Project Structure
```
code-explainer
├── llm-api
│   ├── main.py          # FastAPI application for code explanation
│   ├── requirements.txt # Python dependencies for llm-api
│   └── README.md        # Documentation for llm-api
├── src
│   ├── extension.ts     # Main entry point for the VS Code extension
│   └── README.md        # Documentation for the src directory
├── package.json         # Configuration for npm
├── tsconfig.json        # TypeScript configuration
└── README.md            # Main documentation for the project
```

## Installation

### Prerequisites
- Node.js and npm installed on your machine.
- Python 3.7 or higher installed.
- A compatible language model file for the llm-api.

### Setup
1. Clone the repository:
   ```
   git clone <repository-url>
   cd code-explainer
   ```

2. Install the Python dependencies for the llm-api:
   ```
   cd llm-api
   pip install -r requirements.txt
   ```

3. Install the VS Code extension dependencies:
   ```
   cd ../
   npm install
   ```

## Usage
1. Start the FastAPI server:
   ```
   cd llm-api
   uvicorn main:app --host 127.0.0.1 --port 8000 --reload
   ```

2. Open Visual Studio Code and load the extension:
   - Press `F5` to run the extension in a new Extension Development Host.

3. Use the command palette (`Ctrl+Shift+P`) to access the extension commands and analyze your code snippets.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your branch and create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.