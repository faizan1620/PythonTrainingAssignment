from fastapi import FastAPI
from models.model import Titanic
import pickle

description = """
This API helps you do awesome stuff. 🚀

##It will serve trained model using logistic regression on titanic dataset and predict survival based on real world data
"""

app = FastAPI(title="Predict the survival using Logistic regression",
    description=description,
    version="0.0.1")

@app.get('/')
def root():
    return { 'status': 'FastAPI is running' }

@app.post('/predict')
def predict(req: Titanic):
    filename = './training/finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    feature_data = [[req.Age, req.Fare, req.TravelAlone, req.Pclass_1, req.Pclass_2, req.Embarked_C, req.Embarked_S, req.Sex_male, req.IsMinor]]
    result = loaded_model.predict(feature_data)
    response = 'Survived' if result[0] else 'Not survived'
    return {'Prediction response': response}