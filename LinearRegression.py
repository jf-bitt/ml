# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv(r"C:\Users\joseph.foley\Downloads\linear_data.csv")

x = np.array(data[['x1','x2','x3']])
y = np.array(data[['y']])


inter_ = np.array([np.ones(len(y))])


x = np.append(inter_.T, x, axis=1)


class LinearRegression:
    
    
    def __init__(self,X_train, y_train, max_iter=500, lr=0.0001):
        self.X_train = X_train
        self.y_train = y_train
        self.max_iter = max_iter
        self.lr = lr


    def fit(self, X_train, y_train):
        empty_theta=np.zeros([len(X_train[0])+1, 1])
        coefficients = self.gradient_descent(X_train, y_train, theta=empty_theta)
        return coefficients

    def gradient_descent(self, X_train, y_train, theta):
        n = len(y_train)
        cost_history = np.zeros(self.max_iter)
        theta_history = np.zeros((self.max_iter, len(X_train[0])+1))
        
        inter_ = np.array([np.ones(n)])

        X_train = np.append(inter_.T, X_train, axis=1)

        for i in range(self.max_iter):
            y_pred = np.dot(X_train, theta)
            
            theta = theta - (self.lr/ n)*(np.dot(X_train.T,y_pred-np.array([y_train]).T))
            
            theta_history[i, :] = theta.T

            cost = (1 / (2 * n)) * np.sum(np.square(y_pred - np.array([y_train]).T))
            cost_history[i] = cost
            
            if abs(all((self.lr/ n)*(np.dot(X_train.T,y_pred-np.array([y_train]).T))) <10**-3):
                print(True)
                break

        print("theta = {}"
              .format(theta))

        return theta

    def predict(self, X_test):
        predictions = []
        inter_ = np.array([np.ones(len(X_test))])
        coef = self.fit(self.X_train, self.y_train)
        X_test = np.append(inter_.T, X_test, axis=1)
        for value in X_test:
            predictions.append((np.dot(value, coef))[0])
        print(predictions)
        return predictions



x = np.array(data[['x1','x2','x3']])
y = np.array(data['y'])

x2 = np.array([[10, 10, 10],[20,20,20]])
lr = LinearRegression(x, y)

coef = lr.fit(x, y)


predict = lr.predict(x2)


check = np.array([[0.001,0.002,0.003],[0.004,0.005,0.006]])
