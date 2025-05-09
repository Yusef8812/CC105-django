import os  # Import os module
import joblib
import pandas as pd
from pathlib import Path
from django.conf import settings  

model_path = os.path.join(settings.BASE_DIR, 'predictor', 'final_model.pkl')
model = joblib.load(model_path)


def make_prediction(data):
    """
    Make a prediction using the loaded model.
    :param data: A dictionary of input features.
    :return: The prediction result.
    """
    df = pd.DataFrame([data])  
    prediction = model.predict(df)
    return prediction[0]