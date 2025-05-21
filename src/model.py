import pandas as pd
import requests
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from dotenv import load_dotenv
import os

def predict(token: str):
    load_dotenv()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    api_url = os.getenv("API_URL") 
    fetch_data = requests.get(api_url, headers=headers)
    if fetch_data:
        df = pd.DataFrame(fetch_data.json())
        
        if df.isna().any().any():
            print("Missing data detected. Handling missing values...")
            df = df.dropna()
        
        df.drop(['_id', 'phone'], inplace=True, axis=1)
        
        label_encoder = LabelEncoder()
        for col in df.columns:
            df[col] = label_encoder.fit_transform(df[col])
        
        X = df.drop('interested_to_buy', axis=1)
        y = df['interested_to_buy']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.3,random_state=42)
        
        rfc = RandomForestClassifier()
        rfc.fit(X_train, y_train)
        
        rfc.predict(X_test)
        
        return "done"
    else:
        return "Failed to predict"
