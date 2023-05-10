# Titanic dataset training using logistic regression

Trained a logistic regression model and saved it to disk.

Created a FastAPI service which serves the model as an endpoint. Input to the API should be a JSON object containing a single passenger information. Output can be a simple Yes/No predicting their survival.

### Endpoints 

|HTTP Method|URL|Description|
|---|---|---|
|`GET`|http://localhost:8000/ | Root page |
|`GET`|http://localhost:8000/predict | Get prediction of survival of the passenger based on passenger's information |

### Run

```
https://localhost:8000/docs
```

### Test

You can run the test cases also using pytest using command:

```
python3 -m pytest
```


