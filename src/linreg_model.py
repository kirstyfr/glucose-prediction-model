import pandas as pd
from math import sqrt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def split_data(df, test_size, random_state):
    # Splitting variables, glucose = independent/current = dependent
    X = df[['substrate_reference_mM']] 
    y = df['current_nA'] 
    # Split dataset into test/train
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train, model=None):
    """
    Train a regression model. When no model specified use LinearRegression.
    Parameters:
    X_train: Training features (glucose)
    y_train: Training targets (current)
    model: (optional) A model instance with a .fit() method (LinearRegression is default)
    """
    # Use the provided model if one is given, otherwise default to LinearRegression
    if model is None:
        model = LinearRegression()
    
    # Fit the model using X = glucose (feature) and y = current (target)
    model.fit(X_train, y_train)
    
    return model


def evaluate_model(regressor, X_test, y_test):
    # create predictions on test dataset
    y_pred = regressor.predict(X_test)     # predicted value of y_test
    # create dictionary of all evaluation metrics
    evaluation_metrics = {
        "mae" : float(mean_absolute_error(y_test,y_pred)),
        "mse" : float(mean_squared_error(y_test,y_pred)),
        "rms" : sqrt(mean_squared_error(y_test, y_pred)),
        "r2" : r2_score(y_test, y_pred),
        "coefficient" : float(regressor.coef_[0]),
        "intercept" : float(regressor.intercept_)
    }
    return evaluation_metrics
