# ML on IRIS dataset (FastAPI)

Applying deifferent machine learning algorithms to train and predict on IRIS dataset.

## Overview

#### Pre Requirements

* Python3
* pip

### SETUP

1. Create a virtual env in python

   ```
   python -m venv /path/to/new/virtual/environment
   ```
2. Activate that virtual environment

   ```
   source /path_to_new_virtual_environment/bin/activate
   ```
3. Install required packages using command:

   ```
   $ pip install -r requirements.txt
   ```
   ```
4. Now start the server by running the command:

   ```
   uvicorn main:app
   ```

   Now FastAPI server got started
5. Use this URL to open swagger-UI inorder to test the endpoints

   ```
    localhost:8000/docs
   ```

   You can also use Postman to test the routes/endpoints

### Endpoints

| HTTP Method | URL                                                                                                             | Description                               |
| ----------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| `GET`     | [http://localhost:8000/](http://localhost:8000/ "http://localhost:8000/")                                             | Root page                                 |
| `GET`     | [http://localhost:8000/k_means](http://localhost:8000/k_means "http://localhost:8000/k_means/")                        | K Means plot for iris dataset created and saved               |
| `GET`     | [http://localhost:8000/logistic_regression](http://localhost:8000/logistic_regression "http://localhost:8000/logistic_regression") | Model trained using logistic regression and get prediction for your feature (Query params:sepal_length:float, sepal_width:float, petal_length:float, petal_width:float )              |
| `GET`    | [http://localhost:8000/xgboost_classifier](http://localhost:8000/xgboost_classifier "http://localhost:8000/xgboost_classifier")                        | Model trained using xgboost classifier and get prediction for your feature (Query params:sepal_length:float, sepal_width:float, petal_length:float, petal_width:float )          |
| `GET`     | [http://localhost:8000/decision_tree_classifier](http://localhost:8000/decision_tree_classifier "http://localhost:8000/decision_tree_classifier") | Model trained using decision tree classifier and get prediction for your feature (Query params:sepal_length:float, sepal_width:float, petal_length:float, petal_width:float)       |
| `GET`  | [http://localhost:8000/random_forest_classifier](http://localhost:8000/random_forest_classifier "http://localhost:8000/random_forest_classifier") | Model trained using random forest classifier and get prediction for your feature (Query params:sepal_length:float, sepal_width:float, petal_length:float, petal_width:float)       |
| `GET`     | [http://localhost:8000/adaboost_classifier](http://localhost:8000/adaboost_classifier "http://localhost:8000/adaboost_classifier")                                 | Model trained using adaboost classifier and get prediction for your feature (Query params:sepal_length:float, sepal_width:float, petal_length:float, petal_width:float)                  |
| `GET`     | [http://localhost:8000/svm_classifier](http://localhost:8000/svm_classifier "http://localhost:8000/svm_classifier")          | Model trained using svm classifier and get prediction for your feature (Query params:sepal_length:float, sepal_width:float, petal_length:float, petal_width:float)                 |
| `GET`     | [http://localhost:8000/k_neighbors_classifier](http://localhost:8000/k_neighbors_classifier "http://localhost:8000/k_neighbors_classifier")    | Model trained using k neighbors classifier and get prediction for your feature (Query params:sepal_length:float, sepal_width:float, petal_length:float, petal_width:float) |

### Test

You can run the test cases also using pytest using command:

```
python3 -m pytest
```
