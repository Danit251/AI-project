import calculate_features
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn.preprocessing import MinMaxScaler


# 'C',
# 'max_iter',
# 'shrinking',
# 'cache_size',
# 'class_weight',
# 'decision_function_shape',
# 'random_state',
# 'kernel',
# 'probability',
# 'gamma',
# 'coef0',
# 'tol',
# 'degree',
# 'verbose'


parameters = {
    # 'kernel': ('linear', 'rbf', 'poly'),
    # 'C': [0.5, 1.5, 10, 100, 1000, 5000, 10000, 30000, 70000, 140000],
    # 'gamma': [1e-12, 1e-11, 1e-7, 1e-4, 1e-2, 0.2, 1e-10, 0.007]

    # todo maybe should increase C value?
    'kernel': ('linear'),
    'C': [140000],
    'gamma': [1e-12]
}

if __name__ == '__main__':
    data = calculate_features.create_corpus_vector()
    X = data[:, 0]
    y = data[:, 1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    # clf = GridSearchCV(svm.SVC(), parameters)

    # scaling to (-1,1) range
    scaling = MinMaxScaler(feature_range=(-1, 1)).fit(X_train)
    X_train = scaling.transform(X_train)
    X_test = scaling.transform(X_test)

    clf = svm.SVC(kernel='linear', C=140000, gamma=1e-12)
    # train
    clf.fit(np.ndarray.tolist(X_train), np.ndarray.tolist(y_train))
    # test
    predicted = clf.predict(np.ndarray.tolist(X_test))
    print(clf.score(np.ndarray.tolist(X_test), np.ndarray.tolist(y_test)))
    # print(clf.best_params_)
