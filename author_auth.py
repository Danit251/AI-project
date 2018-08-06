import argparse
import util
import calculate_features
import graphs



def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-authors_num',
                        type=check_range,
                        default=util.authors_num,
                        help="The number of authors to train over.")
    parser.add_argument('-test',
                        type=float,
                        default=0.2,
                        help="The ratio of test split.")
    parser.add_argument('-algo_list',
                        nargs='+',
                        default=['DT', 'RF', 'SVM'],
                        help="List of algorithms to apply. Currently supporting {}".format(util.AVAILABLE_ALGORITHMS.keys()))
    parser.add_argument('-split_by_book',
                        action='store_true',
                        help='split the data where a new book will be in the test')
    return parser, parser.parse_args()


def check_range(value):
    ivalue = int(value)
    if ivalue <= 0 or ivalue >= util.authors_num:
         raise argparse.ArgumentTypeError("{} is an invalid authors int value, only at range 0 to {}".
                                          format(value, util.authors_num))
    return ivalue


if __name__ == "__main__":

    parser, args = parse_arguments()

    for algo in args.algo_list:
        if algo.upper() not in util.AVAILABLE_ALGORITHMS:
            parser.error("{} algorithm is not supported, try from {}".format(algo, util.AVAILABLE_ALGORITHMS.keys()))
    # run each algorithm
    data = calculate_features.create_corpus_vector(args.authors_num)
    for algo in args.algo_list:
        util.AVAILABLE_ALGORITHMS[algo].run(args.test, data, args.split_by_book)


    # graphs.authors_num_to_success_ratio(args.test)
