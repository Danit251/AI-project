import matplotlib.pyplot as plt
import util
import calculate_features
import numpy as np


def authors_num_to_success_ratio(test_ratio):
    scores = np.zeros((len(util.AVAILABLE_ALGORITHMS), util.authors_num - 1))
    for i in range(2, util.authors_num + 1):
        data = calculate_features.create_corpus_vector(i)
        for name, algo in util.AVAILABLE_ALGORITHMS.items():
            scores[util.ALGORITHMS_NUMS[name], i-2] = (algo.run(test_ratio, data)[1])

    for name in util.AVAILABLE_ALGORITHMS.keys():
        plt.plot(list(range(2, util.authors_num + 1)), scores[util.ALGORITHMS_NUMS[name]], label=name)
    plt.legend()
    plt.show()

