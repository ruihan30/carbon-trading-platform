# Activate virtual environment
Write-Host "Activating virtual environment..."
.\venv\Scripts\Activate.ps1

# Optional: create tables (only for dev)
# Write-Host "Creating database tables if they don't exist..."
# python create_tables.py

# Start FastAPI backend
Write-Host "Starting FastAPI backend..."
uvicorn app.main:app --reload
