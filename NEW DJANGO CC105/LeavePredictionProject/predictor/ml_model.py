import joblib
import os

MODEL_FILE = os.path.join(os.path.dirname(__file__), 'final_model.pkl')
model = joblib.load(MODEL_FILE)