from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_logistic_regression_predict():
    response = client.get("/logistic_regression?sepal_length=4.5&sepal_width=2.6&petal_length=2.5&petal_width=1.2")
    assert response.status_code == 200
    assert response.json() == {'status': 'Logistic Regression predicted as: setosa'}

def test_xgboost_predict():
    response = client.get("/xgboost_classifier?sepal_length=2.5&sepal_width=5.6&petal_length=3&petal_width=1.2")
    assert response.status_code == 200
    assert response.json() == {'status': 'XGboost classifier predicted as: versicolor'}

def test_decision_tree_classifier_predict():
    response = client.get("/decision_tree_classifier?sepal_length=1.1&sepal_width=1.2&petal_length=1.1&petal_width=1")
    assert response.status_code == 200
    assert response.json() == {'status': 'Decision tree classifier predicted as: versicolor'}

def test_random_forest_classifier_predict():
    response = client.get("/random_forest_classifier?sepal_length=3.5&sepal_width=1.6&petal_length=6.5&petal_width=3.2")
    assert response.status_code == 200
    assert response.json() == {'status': 'Random forest classifier predicted as: virginica'}

def test_adaboost_classifier_predict():
    response = client.get("/adaboost_classifier?sepal_length=3.5&sepal_width=1&petal_length=3&petal_width=3.2")
    assert response.status_code == 200
    assert response.json() == {'status': 'Adaboost classifier predicted as: virginica'}

def test_svm_classifier_predict():
    response = client.get("/svm_classifier?sepal_length=4.5&sepal_width=2.6&petal_length=2.5&petal_width=1.2")
    assert response.status_code == 200
    assert response.json() == {'status': 'SVM classifier predicted as: versicolor'}

def test_kneighbors_classifier_predict():
    response = client.get("/k_neighbors_classifier?sepal_length=1.5&sepal_width=1.6&petal_length=2.5&petal_width=2.2")
    assert response.status_code == 200
    assert response.json() == {'status': 'K neighbors classifier predicted as: versicolor'}