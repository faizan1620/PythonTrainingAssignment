from sklearn.tree import DecisionTreeClassifier


def decision_tree_train(df):
    X_train = df.drop(["target"], axis=1)
    y_train = df["target"]

    # Instantiate the model
    cls = DecisionTreeClassifier()

    # Train/Fit the model
    cls.fit(X_train, y_train)
    return cls


def decision_tree_predict(cls, iris, X_pred):
    targets = iris.target_names
    print(targets)
    # Make prediction using the model
    y_pred = cls.predict([X_pred])

    print("Prediction is: {}".format(targets[y_pred]))
    return targets[y_pred][0]
