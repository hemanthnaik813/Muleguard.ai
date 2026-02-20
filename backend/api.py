from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Muleguard Backend Running Successfully 🚀"}

@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(upload_dir, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

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
        return JSONResponse(status_code=500, content={"error": str(e)})