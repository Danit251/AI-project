import matplotlib.pyplot as plt
import util
import calculate_features
import numpy as np


def authors_num(test_ratio):
    scores = np.zeros((len(util.AVAILABLE_ALGORITHMS), util.AUTHORS_NUM - 1))
    for i in range(2, util.AUTHORS_NUM + 1):
        data = calculate_features.create_corpus_vector(authors_num=i)
        for name, algo in util.AVAILABLE_ALGORITHMS.items():
            scores[util.ALGORITHMS_NUMS[name], i-2] = (algo.run(test_ratio, data)[1])

    for name in util.AVAILABLE_ALGORITHMS.keys():
        plt.plot(list(range(2, util.AUTHORS_NUM + 1)), scores[util.ALGORITHMS_NUMS[name]], label=name)
    plt.legend()
    plt.show()


def features():
    scores = np.zeros((len(util.AVAILABLE_ALGORITHMS), util.FEATURES_MODULES_NUMBER))
    features_vectors = [calculate_features.create_corpus_vector(features_mask=[1, 0, 0]),
                        calculate_features.create_corpus_vector(features_mask=[0, 1, 0]),
                        # calculate_features.create_corpus_vector(features_mask=[0, 0, 1])
                        ]
    for i in range(len(features_vectors)):
        for name, algo in util.AVAILABLE_ALGORITHMS.items():
            print(name)
            scores[util.ALGORITHMS_NUMS[name], i] = (algo.run(util.TEST_SIZE, features_vectors[i])[1])
    LABELS = ["Character", "Syntactic", "word"]
    for i, name in enumerate(util.AVAILABLE_ALGORITHMS.keys()):
        plt.bar(np.arange(util.FEATURES_MODULES_NUMBER)+(i/4), scores[util.ALGORITHMS_NUMS[name]], label=name, width=1/4)
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
    plt.bar(range(3), scores)
    plt.xticks(range(3), labels)
    plt.show()


# algorithms()
