# Activate virtual environment
Write-Host "Activating virtual environment..."
.\venv\Scripts\Activate.ps1

# Optional: create tables (only for dev)
# Write-Host "Creating database tables if they don't exist..."
# python create_tables.py

# Start FastAPI backend
Write-Host "Starting FastAPI backend..."
uvicorn app.main:app --reload

curl -X POST http://localhost:8000/users -H "Content-Type: application/json" -d "{\"user_name\":\"Alice\",\"email\":\"alice@test.com\",\"password\":\"password123\",\"company_uuid\":\"3c1a1b8e-8a94-4d7f-b4a2-2b52fbd8d9f1\"}"

