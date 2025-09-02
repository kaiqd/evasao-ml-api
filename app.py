from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np

# Carrega o modelo 
MODEL_PATH = "models/EvasaoPredictor.joblib"
model = joblib.load(MODEL_PATH)

FEATURES = ["faltas", "nota_media", "horas_trabalho", "idade"]  # mesma ordem utilizada no treino
MODEL_VERSION = "xgb_v1"

app = FastAPI(title="Evasao API", version="1.0")

# CORS (restringir em producao)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

class InputAluno(BaseModel):
    faltas: float = Field(..., ge=0)
    nota_media: float = Field(..., ge=0, le=100)
    horas_trabalho: float = Field(..., ge=0)
    idade: float = Field(..., ge=10, le=100)

class PredictRequest(BaseModel):
    alunos: list[InputAluno]

class PredictResponseItem(BaseModel):
    risk_score: float
    model_version: str

class PredictResponse(BaseModel):
    results: list[PredictResponseItem]

@app.get("/health")
def health():
    return {"status": "ok", "model_version": MODEL_VERSION}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    X = np.array([[getattr(a, f) for f in FEATURES] for a in req.alunos], dtype=float)
    proba = model.predict_proba(X)[:, 1]
    return {"results": [{"risk_score": float(p), "model_version": MODEL_VERSION} for p in proba]}