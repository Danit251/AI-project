import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
import graphviz
# import util
from src.features import calculate_features


def run(util, test_ratio, data, split_by_book=False, repeat=False):
    """
    Run the Decision Tree algorithm on the data
    :param util: a library contains dictionaries used in the algorithm
    :param test_ratio: what is the percentage of the corpus is the test part
    :param data: the corpus features' vector
    :param split_by_book: indicates if to split the data to train-test
            where a entirely new book is only in the test part.
    :param repeat: if needed to repeat the algorithm
    :return: classifier, result
    """
    run_count = 0
    score_sum = 0
    if repeat:
        num_of_runs = util.REPEAT_ITERATION['DT']
    else:
        num_of_runs = 1

    # Calculates DT number of times
    while run_count < num_of_runs:

        # Splits the data to train and test
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

        clf = tree.DecisionTreeClassifier(criterion='entropy', max_features=38, max_depth=5)

        # train
        clf.fit(np.ndarray.tolist(X_train), np.ndarray.tolist(y_train))

        # test
        score = clf.score(np.ndarray.tolist(X_test), np.ndarray.tolist(y_test))

        if repeat:
            print('Iteration {} of Decision Tree resulted score of: {}\n'.format(run_count, score))

        score_sum += score
        run_count += 1

        # export_tree(clf, training_data)

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


def export_tree(clf, training_data):
    """
    export the visualization of the decision tree into readable PDF
    :param clf: decision tree classifier
    :param training_data:
    """
    feature_names = calculate_features.feature_names_vector()
    authors = get_names_of_authors(training_data)
    dot_data = tree.export_graphviz(clf, out_file=None, feature_names=feature_names, class_names=authors)
    graph = graphviz.Source(dot_data)
    graph.render("dt")
