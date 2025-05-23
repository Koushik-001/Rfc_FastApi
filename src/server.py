from fastapi import FastAPI, Request,Query
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
    
#cron job, not needed but for reference if needed
# @app.on_event("startup")
# @repeat_every(seconds= 3 * 60 * 60)
# async def corn_job():
#     train_cron_path()

@app.get('/train/{phone}/{token}')
async def train_cron_path(phone:str,token:str):
    return  model_training(phone,token)

#works fine but any symbols present in phone number dont get registered, addition work needed
# @app.get('/train')
# async def train_cron_query(phone:str = Query(...)):
#     return  model_training(phone)
