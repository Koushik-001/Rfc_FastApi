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
    return predict("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2ODE5YWU2ZjhlZGE5ZmIxOGE4MDVmNDkiLCJwaG9uZSI6Iis5MTkxMDA5NTI3NTIiLCJpYXQiOjE3NDc4MTg2MDcsImV4cCI6MTc0NzkwNTAwN30.KfUObHb66w_taI2dhz4edTOzrfEOGPO35I2gFwdXK1U")
    
