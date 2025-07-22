# Code Explainer Extension

## Overview

The Code Explainer Extension is a Visual Studio Code extension designed to assist developers by providing explanations for code snippets using a language model. This extension leverages a FastAPI backend to process requests and generate concise explanations, making it easier for users to understand complex code.

## Purpose

The `src` directory contains the main entry point for the VS Code extension, which initializes the extension, registers commands, and manages user interactions. This documentation outlines the purpose of the extension and provides guidelines for contributing to the project.

## Features

- Analyze and explain code snippets using a language model.
- User-friendly interface for easy interaction.
- FastAPI backend for processing requests.

## Installation

To install the Code Explainer Extension, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd code-explainer
   ```

3. Install the required dependencies:
   ```
   npm install
   ```

4. Start the extension in Visual Studio Code.

## Usage

Once the extension is installed, you can use it to explain code snippets by:

1. Selecting the code you want to analyze.
2. Invoking the command to explain the selected code.
3. Viewing the generated explanation in the output panel.

## Contributing

Contributions are welcome! If you would like to contribute to the Code Explainer Extension, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch and create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.