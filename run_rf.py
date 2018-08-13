import calculate_features
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
import util


# 'min_weight_fraction_leaf',
# 'class_weight',
# 'min_samples_split',
# 'max_depth',
# 'criterion',
# 'min_samples_leaf',
# 'random_state',
# 'max_features',
# 'min_impurity_split',
# 'max_leaf_nodes',
# 'splitter',
# 'presort'


parameters = {
    'max_depth': [1, 2, 3, 4, 5],
    'max_features': [1, 2, 3, 4]
}


def run(test_ratio, data, split_by_book=False, repeat=False):
    run_count = 0
    score_sum = 0
    if repeat:
        num_of_runs = util.REPEAT_ITERATION['RF']
    else:
        num_of_runs = 1
    while run_count < num_of_runs:
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
        clf = GridSearchCV(RandomForestClassifier(), parameters)
        # train
        clf.fit(np.ndarray.tolist(X_train), np.ndarray.tolist(y_train))
        # test
        score = clf.score(np.ndarray.tolist(X_test), np.ndarray.tolist(y_test))
        if repeat:
            print('Iteration {} of Random Forest resulted score of: {}\n'.format(run_count, score))
        score_sum += score
        run_count += 1
    return clf, score_sum / num_of_runs

    # print(clf.best_estimator_.feature_importances_)
