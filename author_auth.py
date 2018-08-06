import argparse
import os
import run_svm, run_dt, run_rf
import calculate_features

AVAILABLE_ALGORITHMS = {'DT': run_dt, 'RF': run_rf, 'SVM': run_svm}


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-authors_num',
                        type=check_range,
                        default=len(os.listdir("corpus/data")),
                        help="The number of authors to train over.")
    parser.add_argument('-test',
                        type=float,
                        default=0.2,
                        help="The ratio of test split.")
    parser.add_argument('-algo_list',
                        nargs='+',
                        default=['DT', 'RF', 'SVM'],
                        help="List of algorithms to apply. Currently supporting {}".format(AVAILABLE_ALGORITHMS.keys()))
    return parser, parser.parse_args()


def check_range(value):
    ivalue = int(value)
    if ivalue <= 0 or ivalue >= len(os.listdir("corpus/data")):
         raise argparse.ArgumentTypeError("{} is an invalid authors int value, only at range 0 to {}".
                                          format(value, len(os.listdir("corpus/data"))))
    return ivalue


if __name__ == "__main__":

    parser, args = parse_arguments()

    for algo in args.algo_list:
        if algo.upper() not in AVAILABLE_ALGORITHMS:
            parser.error("{} algorithm is not supported, try from {}".format(algo, AVAILABLE_ALGORITHMS.keys()))
    # run each algorithm
    data = calculate_features.create_corpus_vector(args.authors_num)
    for algo in args.algo_list:
        AVAILABLE_ALGORITHMS[algo].run(args.test, data)
        # AVAILABLE_ALGORITHMS[algo].run2()
