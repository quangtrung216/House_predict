from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load model pipeline (encoder + scaler + model)
model = joblib.load("bengaluru_price_model.pkl")

app = FastAPI(
    title="Bengaluru House Price Prediction API",
    description="Nhập các feature → trả về giá nhà dự đoán",
    version="1.0"
)

# Input format phải khớp với các cột X khi bạn train model
class HouseInput(BaseModel):
    location: str
    total_sqft: float
    bath: float
    bhk: float

@app.post("/predict")
def predict_price(data: HouseInput):
    # Convert input → DataFrame
    df = pd.DataFrame([data.dict()])

    # Prediction
    predicted_price = model.predict(df)[0]

    return {
        "input": data.dict(),
        "predicted_price_lakhs": float(predicted_price)  # đơn vị lakh như dataset
    }
