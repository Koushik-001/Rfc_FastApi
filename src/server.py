from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model.train_model import model_training
from model.predict import predict
from fastapi_utils.tasks import repeat_every

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
async def predict_endpoint(response:Request):
    data = await response.json()
    return predict(data)
    
@app.on_event("startup")
@repeat_every(seconds=60)
async def train_cron():
    return  model_training()