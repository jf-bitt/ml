import numpy as np
from matplotlib import pyplot as plt


class LinearRegression:

    def __init__(self, X, y):
        self.X = X
        self.y = y

    def fit(self, X_train, y_train):
        coefficients = self.gradient_descent(X_train, y_train, theta=np.zeros([len(X_train[0]), 1]), lr=0.001, max_iter=1000)
        return coefficients

    def gradient_descent(self, X_train, y_train, theta, lr=0.001, max_iter=1000):
        n = len(y_train)
        cost_history = np.zeros(max_iter)
        theta_history = np.zeros((max_iter, len(X_train[0])))

        for i in range(max_iter):
            y_pred = np.dot(X_train, theta)

            theta = theta - (1 / n) * lr * (X_train.T.dot((y_pred - y_train)))
            theta_history[i, :] = theta.T

            cost = (1 / (2 * n)) * np.sum(np.square(y_pred - y_train))
            cost_history[i] = cost

            # if abs((1 / n) * lr * (X_train.T.dot((y_pred - y_train)))).any() < 10**-2:
            #     print('Decrease is too small, close to convergence')
            #     print((1 / n) * lr * (X_train.T.dot((y_pred - y_train))))
            #     break

        # print("cost history = {}, theta = {}, predicted y = {} "
        #       .format(cost_history, theta, y_pred))

        return theta

    def predict(self, X_test):
        i = 0
        predictions = []
        coef = self.fit(self.X, self.y)
        for value in X_test:
            predictions.append((np.dot(value, coef))[0])
        return predictions


x = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
y = np.array([[15], [30]])

lr = LinearRegression(x, y)

coef = lr.fit(x, y)

y_pred = lr.predict(x)

print(y_pred)
