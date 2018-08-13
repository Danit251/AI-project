import calculate_features
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import tree, ensemble
import util
import graphviz

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


def run(test_ratio, data, split_by_book=False, repeat=False, feature_names=[]):
    run_count = 0
    score_sum = 0
    if repeat:
        num_of_runs = util.REPEAT_ITERATION['DT']
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
        # if you want to play with it.
        # clf = GridSearchCV(tree.DecisionTreeClassifier(criterion='entropy'), parameters)
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_features=4, max_depth=4)
        # train
        clf.fit(np.ndarray.tolist(X_train), np.ndarray.tolist(y_train))
        # test
        score = clf.score(np.ndarray.tolist(X_test), np.ndarray.tolist(y_test))
        if repeat:
            print('Iteration {} of Decision Tree resulted score of: {}\n'.format(run_count, score))
        score_sum += score
        run_count += 1


        # print the tree
        authors = get_names_of_authors(data)
        dot_data = tree.export_graphviz(clf, out_file=None, feature_names=feature_names, class_names=authors)
        graph = graphviz.Source(dot_data)
        graph.render("dt")

    return clf, score_sum / num_of_runs


def get_names_of_authors(data):
    # this is not very efficient because it probably could have been done earlier, when the data vector was created,
    #  but I think it is simpler and not that bad in terms of running time.
    authors = []
    last_author = ""
    for tuple in data:
        author = tuple[1]
        if author != last_author:
            authors.append(author)
            last_author = author
    return authors