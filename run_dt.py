import calculate_features
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import tree, ensemble
# import graphviz

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


def run(test_ratio, data):
    X = data[:, 0]
    y = data[:, 1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_ratio, random_state=0)
    clf = GridSearchCV(tree.DecisionTreeClassifier(criterion='entropy'), parameters)
    # train
    clf.fit(np.ndarray.tolist(X_train), np.ndarray.tolist(y_train))
    # test
    predicted = clf.predict(np.ndarray.tolist(X_test))
    print(clf.score(np.ndarray.tolist(X_test), np.ndarray.tolist(y_test)))

    # print the tree
    # dot_data = tree.export_graphviz(clf.best_estimator_, out_file=None)
    # graph = graphviz.Source(dot_data)
    # graph.render("dt")
