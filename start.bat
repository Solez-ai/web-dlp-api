@echo off
REM Windows batch script to start both worker and API server

echo Starting web-dlp API...
echo.

REM Start worker in background
start /B python -m app.worker

REM Wait a moment
timeout /t 2 /nobreak >nul

REM Start API server
echo API server starting on http://localhost:8000
echo Press Ctrl+C to stop
echo.
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
