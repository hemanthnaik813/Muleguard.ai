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
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # TEMP: Return dummy analysis structure so frontend works
        return {
            "suspicious_accounts": [],
            "fraud_rings": [],
            "summary": {
                "total_accounts_analyzed": 0,
                "total_transactions": 0,
                "processing_time_seconds": 0
            },
            "raw_transactions": []
        }

    except Exception as e:
        return {"error": str(e)}