import argparse
import util
import calculate_features
import nltk

CBLUEBG = '\33[40m'
CEND = '\33[0m'


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
                        default=['DT', 'RF', 'NN'],
                        help="List of algorithms to apply. Currently supporting {}".format(util.AVAILABLE_ALGORITHMS.keys()))
    parser.add_argument('-split_by_book',
                        action='store_true',
                        help='split the data where a new book will be in the test')
    parser.add_argument('-repeat',
                        action='store_true',
                        help='run each algorithm several times and get the average result')
    parser.add_argument('-no_nltk_dwn',
                        action='store_true',
                        help='Will not download nltk\'s packages')
    return parser, parser.parse_args()


def check_range(value):
    ivalue = int(value)
    if ivalue <= 0 or ivalue >= util.AUTHORS_NUM:
         raise argparse.ArgumentTypeError("{} is an invalid authors int value, only at range 0 to {}".
                                          format(value, util.AUTHORS_NUM))
    return ivalue


if __name__ == "__main__":

    parser, args = parse_arguments()
    result_file = open("results.txt", "w")

    for algo in args.algo_list:
        if algo.upper() not in util.AVAILABLE_ALGORITHMS:
            parser.error("{} algorithm is not supported, try from {}\n".format(algo, util.AVAILABLE_ALGORITHMS.keys()))
    # download nltk's
    if not args.no_nltk_dwn:
        nltk.download('stopwords')
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
    print("Collecting and parsing data from ../corpus/data\n")
    data = calculate_features.create_corpus_vector(args.authors_num)
    # run each algorithm
    for algo in args.algo_list:
        clf, score = util.AVAILABLE_ALGORITHMS[algo].run(args.test, data, args.split_by_book, args.repeat)
        if args.repeat:
            res_text = 'Running with {} over {} iterations resulted average score of: '.\
                format(util.ALGORITHMS_NAMES[algo], util.REPEAT_ITERATION[algo], CBLUEBG, str(score), CEND)
        else:
            res_text = 'Running with {} resulted score of: '.\
                format(util.ALGORITHMS_NAMES[algo])
        print('{}{}{}{}\n'.format(res_text, CBLUEBG, str(score), CEND))
        result_file.write('{}{}\n'.format(res_text, str(score)))
    result_file.write("\n")
    result_file.close()
