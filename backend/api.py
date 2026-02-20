# backend/api.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Muleguard AI Backend")

# Enable CORS (important for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Muleguard Backend Running Successfully 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
