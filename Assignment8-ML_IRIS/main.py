from fastapi import FastAPI
from services import load_data,k_means,logistic_regression,xgboost_classifier,decision_tree,random_forest_classifier,adaboost_classifier,svm_classifier,kNeighbors_classifier

description = """
This API helps you do awesome stuff. 🚀

We have applied differenr ML models on IRIS dataset, each served as an endpoint
"""


app = FastAPI(title="ML on IRIS dataset",
    description=description,
    version="0.0.1")

x,df,iris = load_data.load_iris_data()

@app.get('/')
def root():
    return { 'status': 'FastAPI is running' }

@app.get('/k_means')
def k_means_predict():
    try: 
        k_means.k_means_cluster(x,df)
        return {'status': 'K Means clustering plot saved' }
    except Exception as e:
        return { 'error': str(e) }


@app.get('/logistic_regression')
def logistic_regression_predict(sepal_length:float, sepal_width:float, petal_length:float, petal_width:float):
    '''
    Takes sepal_length, sepal_width, petal_length, petal_width as input and predict the label
    '''
    try:
        trained_model = logistic_regression.logistic_regression_train(df)
        X_pred = [sepal_length,sepal_width,petal_length,petal_width]
        predicted_result = logistic_regression.logistic_regression_predict(trained_model,iris,X_pred)
        return { 'status': f'Logistic Regression predicted as: {predicted_result}' }
    except Exception as e:
        return { 'error': str(e) }


@app.get('/xgboost_classifier')
def xgboost_predict(sepal_length:float, sepal_width:float, petal_length:float, petal_width:float):
    '''
    Takes sepal_length, sepal_width, petal_length, petal_width as input and predict the label
    '''
    try:
        trained_model = xgboost_classifier.xgboost_train(df)
        X_pred = [sepal_length,sepal_width,petal_length,petal_width]
        predicted_result = xgboost_classifier.xgboost_predict(trained_model,iris,X_pred)
        return { 'status': f'XGboost classifier predicted as: {predicted_result}' }
    except Exception as e:
        return { 'error': str(e) }


@app.get('/decision_tree_classifier')
def decision_tree_classifier_predict(sepal_length:float, sepal_width:float, petal_length:float, petal_width:float):
    '''
    Takes sepal_length, sepal_width, petal_length, petal_width as input and predict the label
    '''
    try:
        trained_model = decision_tree.decision_tree_train(df)
        X_pred = [sepal_length,sepal_width,petal_length,petal_width]
        predicted_result = decision_tree.decision_tree_predict(trained_model,iris,X_pred)
        return { 'status': f'Decision tree classifier predicted as: {predicted_result}' }
    except Exception as e:
        return { 'error': str(e) }

@app.get('/random_forest_classifier')
def random_forest_classifier_predict(sepal_length:float, sepal_width:float, petal_length:float, petal_width:float):
    '''
    Takes sepal_length, sepal_width, petal_length, petal_width as input and predict the label
    '''
    try:
        trained_model = random_forest_classifier.random_forest_classifier_train(df)
        X_pred = [sepal_length,sepal_width,petal_length,petal_width]
        predicted_result = random_forest_classifier.random_forest_classifier_predict(trained_model,iris,X_pred)
        return { 'status': f'Random forest classifier predicted as: {predicted_result}' }
    except Exception as e:
        return { 'error': str(e) }


@app.get('/adaboost_classifier')
def adaboost_classifier_predict(sepal_length:float, sepal_width:float, petal_length:float, petal_width:float):
    '''
    Takes sepal_length, sepal_width, petal_length, petal_width as input and predict the label
    '''
    try:
        trained_model = adaboost_classifier.adaboost_classifier_train(df)
        X_pred = [sepal_length,sepal_width,petal_length,petal_width]
        predicted_result = adaboost_classifier.adaboost_classifier_predict(trained_model,iris,X_pred)
        return { 'status': f'Adaboost classifier predicted as: {predicted_result}' }
    except Exception as e:
        return { 'error': str(e) }


@app.get('/svm_classifier')
def svm_classifier_predict(sepal_length:float, sepal_width:float, petal_length:float, petal_width:float):
    '''
    Takes sepal_length, sepal_width, petal_length, petal_width as input and predict the label
    '''
    try:
        trained_model = svm_classifier.svm_classifier_train(df)
        X_pred = [sepal_length,sepal_width,petal_length,petal_width]
        predicted_result = svm_classifier.svm_classifier_predict(trained_model,iris,X_pred)
        return { 'status': f'SVM classifier predicted as: {predicted_result}' }
    except Exception as e:
        return { 'error': str(e) }

@app.get('/k_neighbors_classifier')
def kneighbors_classifier_predict(sepal_length:float, sepal_width:float, petal_length:float, petal_width:float):
    '''
    Takes sepal_length, sepal_width, petal_length, petal_width as input and predict the label
    '''
    try:
        trained_model = kNeighbors_classifier.kNeighbors_train(df)
        X_pred = [sepal_length,sepal_width,petal_length,petal_width]
        predicted_result = kNeighbors_classifier.kNeighbors_predict(trained_model,iris,X_pred)
        return { 'status': f'K neighbors classifier predicted as: {predicted_result}' }
    except Exception as e:
        return { 'error': str(e) }

