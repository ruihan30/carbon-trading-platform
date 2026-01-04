from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, balances, requests, users

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(balances.router)
app.include_router(requests.router)
app.include_router(users.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "Backend running"}

@app.get("/test")
def test():
    return {"message": "Connected"}
