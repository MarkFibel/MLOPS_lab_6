from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import logging
from typing import List
import uvicorn
import joblib
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Загрузка модели
try:
    with open("german_v1.joblib", "rb") as f:
        model = pickle.load(f)
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {e}")


# Загрузка scaler (если нужен для обратного преобразования)
try:
    with open("power.joblib", 'rb') as file:
        predict2price = pickle.load(file)
except Exception as e:
    logger.error(f"Error loading scaler: {e}")
    predict2price = None


app = FastAPI(title="Creditability Prediction")


def clear_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df = df[df['Credit_Amount'] >= 0]
    df = df[df['Duration_of_Credit_monthly'] > 0]
    df = df.reset_index(drop=True)
    return df


def featurize(df: pd.DataFrame) -> pd.DataFrame:
    df['Relative_Credit_Amount'] = df['Credit_Amount'] / (df['Account_Balance'] + 1)
    df['Credit_per_month'] = df['Credit_Amount'] / (df['Duration_of_Credit_monthly'] + 1)
    df['Age_at_end_of_credit'] = df['Age_years'] + df['Duration_of_Credit_monthly'] // 12
    df['Credit_per_dependent'] = df['Credit_Amount'] / (df['No_of_dependents'] + 1)
    df['Instalment_to_income_ratio'] = df['Instalment_per_cent'] / (df['Account_Balance'] + 1)
    df['Stability_Index'] = df['Length_of_current_employment'] + df['Duration_in_Current_address']
    df['Has_Guarantor'] = (df['Guarantors'] != 1).astype(int)
    df['Has_Telephone'] = (df['Telephone'] == 1).astype(int)
    df['Is_Foreign_Worker'] = (df['Foreign_Worker'] == 2).astype(int)
    df['Credit_to_age_ratio'] = df['Credit_Amount'] / (df['Age_years'] + 1)
    return df


# Модель входных данных
class CreditFeatures(BaseModel):
    Account_Balance: int
    Duration_of_Credit_monthly: int
    Payment_Status_of_Previous_Credit: int
    Purpose: int
    Credit_Amount: float
    Value_Savings_Stocks: int
    Length_of_current_employment: int
    Instalment_per_cent: float
    Sex_Marital_Status: int
    Guarantors: int
    Duration_in_Current_address: int
    Most_valuable_available_asset: int
    Age_years: int
    Concurrent_Credits: int
    Type_of_apartment: int
    No_of_Credits_at_this_Bank: int
    Occupation: int
    No_of_dependents: int
    Telephone: int
    Foreign_Worker: int

@app.post("/predict", summary="Предсказание кредитоспособности")
async def predict(input: CreditFeatures):
    try:
        input_dict = input.dict()
        df = pd.DataFrame([input_dict])
        df = featurize(df)
        prediction = model.predict(df)[0]
        result = {"creditability_prediction": int(prediction)}
        return result

    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)