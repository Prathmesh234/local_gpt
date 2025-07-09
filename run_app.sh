#!/bin/bash
# Start backend and frontend for local GPT chatbot

# Start backend
uvicorn backend.main:app --reload &
BACKEND_PID=$!

# Start frontend
npm --prefix frontend run dev &
FRONTEND_PID=$!

# Wait for processes
trap 'kill $BACKEND_PID $FRONTEND_PID' EXIT
wait
