import calculate_features
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier


# parameters = {
#     'n_neighbors': [3, 5, 7, 17, 35, 100],
#     'algorithm': ['auto', 'ball_tree', 'kd_tree'],
#     'leaf_size': [50, 10, 75],
#     'p': [1, 3],
#     'n_jobs': [2, 3]
# }


def run(test_ratio, data, split_by_book=False, repeat=False):
    run_count = 0
    score_sum = 0
    if repeat:
        num_of_runs = 100
    else:
        num_of_runs = 1
    while run_count < num_of_runs:
        print("run ", run_count)
        if split_by_book:
            training_data, test_data = calculate_features.split_train_test(data)
            X_train = training_data[:, 0]
            y_train = training_data[:, 1]
            X_test = test_data[:, 0]
            y_test = test_data[:, 1]
        else:
            X = data[:, 0]
            y = data[:, 1]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_ratio)
        clf = KNeighborsClassifier(n_neighbors=5, algorithm='auto', leaf_size=50, n_jobs=2, p=1)
        # train
        clf.fit(np.ndarray.tolist(X_train), np.ndarray.tolist(y_train))
        # test
        score = clf.score(np.ndarray.tolist(X_test), np.ndarray.tolist(y_test))
        score_sum += score
        run_count += 1
        print("score = ", score)
    print("score average = ", score_sum / num_of_runs)
    return clf, score_sum
