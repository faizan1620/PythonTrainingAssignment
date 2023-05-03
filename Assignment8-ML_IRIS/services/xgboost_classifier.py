from xgboost import XGBClassifier
def xgboost_train(df):
    X_train = df.drop(['target'], axis=1).values
    y_train = df['target']

    # Instantiate the model
    cls = XGBClassifier()

    # Train/Fit the model 
    cls.fit(X_train, y_train)
    return cls


def xgboost_predict(cls, iris, X_pred):
    # Make prediction using the model
    targets = iris.target_names
    print(targets)
    y_pred = cls.predict([X_pred])

    print("Prediction is: {}".format(targets[y_pred]))
    return targets[y_pred][0]