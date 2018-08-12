import argparse
import util
import calculate_features
import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')



def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-authors_num',
                        type=check_range,
                        default=util.AUTHORS_NUM,
                        help="The number of authors to train over.")
    parser.add_argument('-test',
                        type=float,
                        default=util.TEST_SIZE,
                        help="The ratio of test split.")
    parser.add_argument('-algo_list',
                        nargs='+',
                        default=['DT', 'RF', 'SVM'],
                        help="List of algorithms to apply. Currently supporting {}".format(util.AVAILABLE_ALGORITHMS.keys()))
    parser.add_argument('-split_by_book',
                        action='store_true',
                        help='split the data where a new book will be in the test')
    parser.add_argument('-repeat',
                        action='store_true',
                        help='run each algorithm several times and get the average result')
    return parser, parser.parse_args()


def check_range(value):
    ivalue = int(value)
    if ivalue <= 0 or ivalue >= util.AUTHORS_NUM:
         raise argparse.ArgumentTypeError("{} is an invalid authors int value, only at range 0 to {}".
                                          format(value, util.AUTHORS_NUM))
    return ivalue


if __name__ == "__main__":

    parser, args = parse_arguments()
    result_file = open("result.txt", "w")

    for algo in args.algo_list:
        if algo.upper() not in util.AVAILABLE_ALGORITHMS:
            parser.error("{} algorithm is not supported, try from {}".format(algo, util.AVAILABLE_ALGORITHMS.keys()))
    # run each algorithm
    data = calculate_features.create_corpus_vector(args.authors_num)
    for algo in args.algo_list:
        clf, score = util.AVAILABLE_ALGORITHMS[algo].run(args.test, data, args.split_by_book, args.repeat)
        result_file.write(algo + " result: " + score + "\n")

    result_file.write("\n")
    result_file.close()