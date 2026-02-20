# backend/api.py

from fastapi import FastAPI
from fastapi import UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

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

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        import pandas as pd
        import io

        # Read file content
        contents = await file.read()

        if not contents:
            return {"error": "Empty file received"}

        # Parse CSV
        df = pd.read_csv(io.BytesIO(contents))

        # Convert to list of dicts
        transactions = df.to_dict(orient="records")

        # Return proper structure expected by frontend
        return {
            "suspicious_accounts": [],
            "fraud_rings": [],
            "summary": {
                "total_accounts_analyzed": len(set(df["sender_id"]).union(set(df["receiver_id"]))),
                "total_transactions": len(df),
                "processing_time_seconds": 1.2
            },
            "raw_transactions": transactions
        }

    except Exception as e:
        return {"error": str(e)}