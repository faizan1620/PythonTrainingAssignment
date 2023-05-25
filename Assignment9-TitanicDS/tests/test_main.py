from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

requestBody = {
    "Age": 25,
    "Fare": 7.1,
    "TravelAlone": 1,
    "Pclass_1": 1,
    "Pclass_2": 0,
    "Embarked_C": 0,
    "Embarked_S": 1,
    "Sex_male": 1,
    "IsMinor": 1,
}


def test_predict():
    response = client.post("/predict", json=requestBody)
    assert response.status_code == 200
    assert response.json() == {"Prediction response": "Survived"}
