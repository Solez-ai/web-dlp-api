#!/bin/bash
# Unix/Linux script to start both worker and API server

echo "Starting web-dlp API..."
echo ""

# Start worker in background
python app/worker.py &

# Wait a moment
sleep 2

# Start API server
echo "API server starting on http://localhost:8000"
echo "Press Ctrl+C to stop"
echo ""
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
