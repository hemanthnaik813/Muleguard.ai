# backend/api.py

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import shutil
import os

app = FastAPI(title="Muleguard AI Backend")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def home():
    return {"message": "Muleguard Backend Running Successfully 🚀"}

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Upload endpoint
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Dummy response for frontend
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
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )