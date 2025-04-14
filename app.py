
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model
model = joblib.load("model_results.pkl")

# Define input schema
class VideoFeatures(BaseModel):
    title_length: int
    title_word_count: int
    title_has_question: int
    title_has_number: int
    description_length: int
    description_has_subscribe: int
    publish_month: int
    publish_hour: int
    like_view_ratio: float
    comment_view_ratio: float
    log_like_count: float
    log_comment_count: float

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "YouTube Video Success Predictor API is running!"}

# Prediction endpoint
@app.post("/predict")
def predict_video_success(features: VideoFeatures):
    input_data = np.array([[
        features.title_length,
        features.title_word_count,
        features.title_has_question,
        features.title_has_number,
        features.description_length,
        features.description_has_subscribe,
        features.publish_month,
        features.publish_hour,
        features.like_view_ratio,
        features.comment_view_ratio,
        features.log_like_count,
        features.log_comment_count
    ]])
    prediction = model.predict(input_data)[0]
    return {"predicted_log_view_count": prediction}




