# FastAPI PyTorch ML Model

This project serves a PyTorch ML model using FastAPI.

## API Endpoint
POST /predict
- Input: JSON list of floats `[1.2, 3.4, ...]`
- Output: `{ "prediction": value }`

## Run Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Deploy
- Push to GitHub
- Deploy on Railway using Dockerfile

