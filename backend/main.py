from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess

app = FastAPI()

class ChatRequest(BaseModel):
    message: str
    model: str = ""

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    if not req.message:
        raise HTTPException(status_code=400, detail="Message is required")
    # Call ollama command line to get a response
    try:
        # Example command: ollama run <model> -p <prompt>
        model = req.model or ""  # default empty
        process = subprocess.run(
            ["ollama", "run", model, "-p", req.message],
            check=True, capture_output=True, text=True
        )
        answer = process.stdout.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return ChatResponse(response=answer)
