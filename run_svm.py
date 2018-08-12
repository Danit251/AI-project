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


def run(test_ratio, data, split_by_book=False):
    if split_by_book:
        training_data, test_data = calculate_features.split_train_test(data)
        X_train = training_data[:, 0]
        y_train = training_data[:, 1]
        X_test = test_data[:, 0]
        y_test = test_data[:, 1]
    else:
        X = data[:, 0]
        y = data[:, 1]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_ratio, random_state=0)
    # clf = GridSearchCV(svm.SVC(), parameters)

    # scaling to (-1,1) range
    # scaling = MinMaxScaler(feature_range=(-1, 1)).fit(X_train)
    # X_train = scaling.transform(X_train)
    # X_test = scaling.transform(X_test)

    clf = svm.SVC(kernel='linear', C=140000, gamma=1e-12)
    # train
    clf.fit(np.ndarray.tolist(X_train), np.ndarray.tolist(y_train))
    # test
    predicted = clf.predict(np.ndarray.tolist(X_test))
    score = clf.score(np.ndarray.tolist(X_test), np.ndarray.tolist(y_test))
    return clf, score
    
#
# def run2(data):
#     print("svm")
#     run = 0
#     score_list = []
#     while run < 10:
#         print(run)
#         training_data, test_data = calculate_features.split_train_test(data)
#         X_train = training_data[:, 0]
#         y_train = training_data[:, 1]
#         X_test = test_data[:, 0]
#         y_test = test_data[:, 1]
#         clf = svm.SVC(kernel='linear', C=140000, gamma=1e-12)
#         # train
#         clf.fit(np.ndarray.tolist(X_train), np.ndarray.tolist(y_train))
#         # test
#         predicted = clf.predict(np.ndarray.tolist(X_test))
#         score = clf.score(np.ndarray.tolist(X_test), np.ndarray.tolist(y_test))
#         score_list.append(score)
#         run += 1
#     print(sum(score_list) / len(score_list))