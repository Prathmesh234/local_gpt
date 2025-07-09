# Local GPT Chatbot

This project provides a lightweight local ChatGPT-like interface. The frontend is built with **React/TypeScript** using Vite and simple shadcn-inspired components. The backend is a minimal **FastAPI** application that calls a local model through **[Ollama](https://ollama.ai/)**.

## Architecture

```
┌──────────┐        HTTP        ┌──────────┐
│ frontend │  <------------->  │ backend  │
└──────────┘                    └──────────┘
                                    │
                                    │ (subprocess)
                                    ▼
                                 Ollama
```

- **Frontend** (`/frontend`)
  - Written in React/TypeScript.
  - Displays chat messages in a modern layout with a text area at the bottom.
  - Sends the user's message to the backend and renders the returned response.
- **Backend** (`/backend`)
  - Provides a `/chat` endpoint implemented with FastAPI.
  - Uses the `ollama` CLI to run a local model and return its response.

## Running

Install Python and Node dependencies (see `requirements.txt` and `frontend/package.json`). Then use the provided script to start both parts:

```bash
./run_app.sh
```

The backend will run on `http://localhost:8000` and the frontend on `http://localhost:3000`.

## Ollama

[Ollama](https://ollama.ai/) allows you to run language models locally. Install it according to their documentation and make sure the `ollama` command is available in your `PATH`. You can specify the model name in the API request; by default the example leaves it empty so you can choose your own.
