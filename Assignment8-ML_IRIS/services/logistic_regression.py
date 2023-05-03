from sklearn.linear_model import LogisticRegression

def logistic_regression_train(df):
    # Let's see a sample of created df
    df.sample(frac=0.01)
    X_train = df.drop(['target'], axis=1)
    y_train = df['target']
    cls = LogisticRegression()
    
    
    # Train/Fit the model 
    cls.fit(X_train, y_train)
    return cls

def logistic_regression_predict(cls, iris, X_pred):
    # Make prediction using the model
    targets = iris.target_names
    y_pred = cls.predict([X_pred])

    print("Prediction is: {}".format(targets[y_pred]))
    return targets[y_pred][0]

