# README for llm-api

## Overview

The `llm-api` is a FastAPI application designed to provide an endpoint for explaining code snippets using a language model. This API leverages the capabilities of the LlamaCpp model to analyze and generate concise explanations for provided code.

## Features

- **Code Explanation**: Submit code snippets and receive brief explanations.
- **FastAPI Framework**: Built using FastAPI for high performance and easy integration.
- **Input Validation**: Utilizes Pydantic for validating incoming requests.

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd code-explainer/llm-api
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Ensure that the model path in `main.py` is correct for your system.

### Running the API

To start the FastAPI application, run the following command:

```
python main.py
```

The API will be available at `http://127.0.0.1:8000/explain`.

### Usage

To use the API, send a POST request to the `/explain` endpoint with a JSON body containing the code snippet you want to explain. For example:

```json
{
  "code": "print('Hello, World!')"
}
```

The response will contain the explanation of the provided code.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.