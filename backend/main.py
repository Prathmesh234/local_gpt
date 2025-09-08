from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess

app = FastAPI()

# Add CORS middleware for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message is required")
    
    try:
        # Call ollama with a simple command structure
        process = subprocess.run(
            ["ollama", "run", "llama2", req.message],
            check=True, 
            capture_output=True, 
            text=True,
            timeout=30
        )
        return ChatResponse(response=process.stdout.strip())
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=408, detail="Request timeout")
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Ollama error: {e.stderr}")
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Ollama not found. Please install Ollama.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
