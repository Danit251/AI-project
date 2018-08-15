import matplotlib.pyplot as plt
import numpy as np
from src import util
from src.features import calculate_features


def authors_num(test_ratio=util.TEST_SIZE):
    scores = np.zeros((len(util.AVAILABLE_ALGORITHMS), util.AUTHORS_NUM - 1))
    for i in range(2, util.AUTHORS_NUM + 1):
        data = calculate_features.create_corpus_vector(authors_num=i)
        for name, algo in util.AVAILABLE_ALGORITHMS.items():
            scores[util.ALGORITHMS_NUMS[name], i-2] = (algo.run(test_ratio, data)[1])

    for name in util.AVAILABLE_ALGORITHMS.keys():
        plt.plot(list(range(2, util.AUTHORS_NUM + 1)), scores[util.ALGORITHMS_NUMS[name]], label=name)
    plt.xlabel('Number of authors')
    plt.ylabel('% correct classifications')
    plt.xticks(range(2, 6))
    plt.axis([2, 5, 0, 1.00])
    plt.legend()
    plt.show()


def features():
    scores = np.zeros((len(util.AVAILABLE_ALGORITHMS), util.FEATURES_MODULES_NUMBER))
    features_vectors = [calculate_features.create_corpus_vector(features_mask=[1, 0, 0]),
                        calculate_features.create_corpus_vector(features_mask=[0, 1, 0]),
                        calculate_features.create_corpus_vector(features_mask=[0, 0, 1])
                        ]
    for i in range(len(features_vectors)):
        for name, algo in util.AVAILABLE_ALGORITHMS.items():
            scores[util.ALGORITHMS_NUMS[name], i] = (algo.run(util.TEST_SIZE, features_vectors[i])[1])
    LABELS = ["Character", "Syntactic", "Word"]
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
    scores = np.zeros(len(util.AVAILABLE_ALGORITHMS))
    data = calculate_features.create_corpus_vector()
    labels = []
    for name, algo in util.AVAILABLE_ALGORITHMS.items():
        scores[util.ALGORITHMS_NUMS[name]] = (algo.run(util.TEST_SIZE, data, repeat=True)[1])
        labels.append(name)
    plt.xlabel('Algorithm')
    plt.ylabel('% correct classifications')
    bar = plt.bar(range(3), scores)
    for rect in bar:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%0.2f' % height, ha='center', va='bottom')
    plt.xticks(range(3), labels)
    plt.show()
