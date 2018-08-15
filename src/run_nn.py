import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from src.features import calculate_features


def run(util, test_ratio, data, split_by_book=False, repeat=False):
    run_count = 0
    score_sum = 0
    if repeat:
        num_of_runs = util.REPEAT_ITERATION['NN']
    else:
        num_of_runs = 1
    # Calculates NN number of times
    while run_count < num_of_runs:

        # Splits data to train and test
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

        if repeat:
            print('Iteration {} of Nearest Neighbors resulted score of: {}\n'.format(run_count, score))

        score_sum += score
        run_count += 1

    if repeat:
        return clf, score_sum / num_of_runs

    return clf, score
