# filepath: c:\Users\dholz\GitRepos\code-explainer\llm-api\main.py
from fastapi import FastAPI
from pydantic import BaseModel
from langchain import LlamaCpp
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import uvicorn

app = FastAPI()
# Make sure the model path is correct for your system!
llm = LlamaCpp(model_path="./llm-api/Phi-3-mini-4k-instruct-q4.gguf",
n_gpu_layers=-1,
max_tokens=500,
n_ctx=2048,
seed=42,
verbose=False,
temperatur = 0
)

class CodeRequest(BaseModel):
    code: str

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant that can analyze and explain code. Important: Keep your answer as short as possible."),
    ("human", "{code}")])

parser = StrOutputParser()

@app.post("/explain")
async def explain_code(request: CodeRequest):
    """Endpoint to explain code snippets."""
    prompt_with_code = prompt.format(code=request.code)
    result = (llm | parser).invoke(prompt_with_code)
    return {"explanation": result}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)