import pandas as pd
import requests
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from dotenv import load_dotenv
import os
import joblib


def model_training(phone:str,token:str):
        load_dotenv()
        api_url = os.getenv("API_URL")

        headers = {"Authorization": f"Bearer {token}"}
        fetch_data = requests.get(f"{api_url}/find_feedback/{phone}", headers=headers)

        if fetch_data:
            df = pd.DataFrame(fetch_data.json())

            df = df.dropna()
            df.drop(['_id', 'phone'], axis=1, inplace=True)

            label_encoder = LabelEncoder()
            for col in df.columns:
                df[col] = label_encoder.fit_transform(df[col])

            X = df.drop('interested_to_buy', axis=1)
            y = df['interested_to_buy']

            X_train, _, y_train, _ = train_test_split(X, y, train_size=0.3, random_state=42)

            model = RandomForestClassifier()
            model.fit(X_train, y_train)

            joblib.dump(model, "model/model.pkl")
            print("✅ Model trained and saved as model.pkl")
            return "Succesfully Trained"
        else:
            print("❌ Failed to fetch training data")
            return "Failed to train"
