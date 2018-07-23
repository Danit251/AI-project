import calculate_features
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn import svm

data = calculate_features.create_corpus_vector()
X = data[:, 0]
y = data[:, 1]
parameters = {'kernel': ('linear', 'rbf', 'poly'), 'C': [0.5, 1.5, 10, 100, 1000, 5000, 10000, 30000, 70000, 140000], 'gamma': [1e-12, 1e-11,1e-7, 1e-4, 1e-2, 0.2,1e-10, 0.007]}
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
svm1 = svm.SVC()
clf = GridSearchCV(svm1, parameters)
a = clf.fit(np.ndarray.tolist(X_train), np.ndarray.tolist(y_train))
# print(clf.predict([[0.4]]))
predicted = clf.predict(np.ndarray.tolist(X_test))
print(clf.best_params_)
print(predicted)
print(clf.score(np.ndarray.tolist(X_test), np.ndarray.tolist(y_test)))
