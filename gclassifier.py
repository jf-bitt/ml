from scipy.spatial import distance
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def euc(a, b):
    return distance.euclidean(a, b)


class ScrappyKNN:
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        y_predictions = []
        for row in X_test:
            label = self.closest(row)
            y_predictions.append(label)
        return y_predictions

    def closest(self, row):
        # best_dist starts from first value within X_train data
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        # loops through the remaining values within X_train
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            # Checks if the dist of new point is closer
            if dist < best_dist:
                # Updates best_dist with new dist if closer
                best_dist = dist
                best_index = i
            # Returns the given y_train value based on index of closest value
        return self.y_train[best_index]


iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.5)

my_classifer = ScrappyKNN()

my_classifer.fit(X_train, y_train)

predictions = my_classifer.predict(X_test)
print(accuracy_score(y_test, predictions))

print(X_train[0], y_train[0])
