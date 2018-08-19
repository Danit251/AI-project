import matplotlib.pyplot as plt
import numpy as np
from src.features import calculate_features
from src import util
import os

LABELS = ["Character", "Syntactic", "Word"]

def authors_num(test_ratio=util.TEST_SIZE):
    scores = np.zeros((len(util.AVAILABLE_ALGORITHMS), util.AUTHORS_NUM - 1))
    for i in range(2, util.AUTHORS_NUM + 1):
        data = calculate_features.get_corpus_vector(False, authors_num=i)
        for name, algo in util.AVAILABLE_ALGORITHMS.items():
            scores[util.ALGORITHMS_NUMS[name], i-2] = (algo.run(util, test_ratio, data)[1])

    for name in util.AVAILABLE_ALGORITHMS.keys():
        plt.plot(list(range(2, util.AUTHORS_NUM + 1)), scores[util.ALGORITHMS_NUMS[name]], label=name)
    plt.xlabel('Number of authors')
    plt.ylabel('% correct classifications')
    plt.xticks(range(2, util.AUTHORS_NUM + 1))
    plt.axis([2, util.AUTHORS_NUM, 0, 1.00])
    plt.legend()
    plt.show()


def feature_importance():
    data = calculate_features.get_corpus_vector(True)
    importances = util.AVAILABLE_ALGORITHMS['RF'].run(util, util.TEST_SIZE, data)[0].feature_importances_
    count = 0
    for feature_class in LABELS:
        plt.bar(range(count, count + util.FEATURE_CLASS_COUNT[feature_class]), importances[count:count+util.FEATURE_CLASS_COUNT[feature_class]], label=feature_class)
        count += util.FEATURE_CLASS_COUNT[feature_class]
    plt.xlabel('Feature number')
    plt.ylabel('% of importance')
    plt.legend()
    plt.show()


def features():
    scores = np.zeros((len(util.AVAILABLE_ALGORITHMS), util.FEATURES_MODULES_NUMBER))
    features_vectors = [calculate_features.get_corpus_vector(False, features_mask=[1, 0, 0]),
                        calculate_features.get_corpus_vector(False, features_mask=[0, 1, 0]),
                        calculate_features.get_corpus_vector(False, features_mask=[0, 0, 1])
                        ]
    for i in range(len(features_vectors)):
        for name, algo in util.AVAILABLE_ALGORITHMS.items():
            scores[util.ALGORITHMS_NUMS[name], i] = (algo.run(util, util.TEST_SIZE, features_vectors[i], repeat=True)[1])

    for i, name in enumerate(util.AVAILABLE_ALGORITHMS.keys()):
        bar = plt.bar(np.arange(util.FEATURES_MODULES_NUMBER)+(i/4), scores[util.ALGORITHMS_NUMS[name]], label=name, width=1/4)
        for rect in bar:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%0.2f' % height, ha='center', va='bottom')
    plt.xlabel('Feature class')
    plt.ylabel('% correct classifications')
    plt.xticks([1 / 4, 5 / 4, 9 / 4], LABELS)
    plt.legend()
    plt.show()


def algorithms():
    """
    Compute the 3 algorithms results over 2 splitting methods.
    :return: Graph that contains 6 results, 3 for each split.
    """
    scores = np.zeros(len(util.AVAILABLE_ALGORITHMS))
    # split_by_book a.k.a spp
    sbb_scores = np.zeros(len(util.AVAILABLE_ALGORITHMS))
    data = calculate_features.get_corpus_vector(True)
    labels = []
    for name, algo in util.AVAILABLE_ALGORITHMS.items():
        scores[util.ALGORITHMS_NUMS[name]] = (algo.run(util, util.TEST_SIZE, data, repeat=True)[1])
        sbb_scores[util.ALGORITHMS_NUMS[name]] = (algo.run(util, util.TEST_SIZE, data, repeat=True, split_by_book=True)[1])
        labels.append(name)
    plt.xlabel('Algorithm')
    plt.ylabel('% correct classifications')
    bars = [plt.bar(range(3), scores), plt.bar(range(3), sbb_scores, label='sbb')]
    for bar in bars:
        for rect in bar:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%0.2f' % height, ha='center', va='bottom')
    plt.legend()
    plt.xticks(range(3), labels)
    plt.show()


# def split_by_book():
#     scores = np.zeros(len(util.AVAILABLE_ALGORITHMS))
#     data = calculate_features.get_corpus_vector(True)
#     labels = []
#     for name, algo in util.AVAILABLE_ALGORITHMS.items():
#         scores[util.ALGORITHMS_NUMS[name]] = (algo.run(util, util.TEST_SIZE, data, repeat=True, split_by_book=True)[1])
#         labels.append(name)
#     plt.xlabel('Algorithm')
#     plt.ylabel('% correct classifications')
#     bar = plt.bar(range(3), scores)
#     for rect in bar:
#         height = rect.get_height()
#         plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%0.2f' % height, ha='center', va='bottom')
#     plt.xticks(range(3), labels)
#     plt.show()
