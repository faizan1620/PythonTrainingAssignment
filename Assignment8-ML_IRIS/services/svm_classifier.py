from sklearn.svm import SVC


def svm_classifier_train(df):
    # Prepare training data for building the model
    X_train = df.drop(["target"], axis=1)
    y_train = df["target"]

    # Instantiate the model
    cls = SVC()

    # Train/Fit the model
    cls.fit(X_train, y_train)
    return cls


def svm_classifier_predict(cls, iris, X_pred):
    targets = iris.target_names
    print(targets)
    # Make prediction using the model
    y_pred = cls.predict([X_pred])

    print("Prediction is: {}".format(targets[y_pred]))
    return targets[y_pred][0]
