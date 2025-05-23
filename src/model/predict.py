import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from dotenv import load_dotenv
import os
import requests


model = joblib.load("model/model.pkl")

def predict(data):
    
        df = pd.DataFrame([data])
        df = df.dropna()
        df.drop([ 'phone'], axis=1, inplace=True)

        label_encoder = LabelEncoder()
        for col in df.columns:
            df[col] = label_encoder.fit_transform(df[col])

        X = df
        predictions = model.predict(X)

        return {"predictions": predictions.tolist()}


