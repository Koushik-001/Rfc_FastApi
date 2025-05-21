from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class JwtToken(BaseModel):
    token: str

@app.get('/')
async def get_fun():
    return {"message": "Hello world"}

@app.post('/predict')
async def predict_endpoint(token: JwtToken):
    return token
