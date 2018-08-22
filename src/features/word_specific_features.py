import string
import nltk
from collections import Counter

FEATURE_NUM = 7


def calculate_words_feature_vector(text):
    """
    :param text: text to vectorize
    :returns vector that represents the word features in the text
    """
    global feature_names
    feature_names = []
    feature_vector = []
    signs = set(string.punctuation)
    signs.remove('.')

    text_without_punc = text
    for sign in signs:
        text_without_punc = text_without_punc.replace(sign, "")

    text_without_dot = text_without_punc.replace(" .", "")
    text_without_spances = text_without_dot.replace(' ', "")
    words = text_without_dot.split(" ")
    words_num = len(words)
    sents_num = text_without_punc.count(" .")
    vector = [num_of_short_words(words),
              num_of_long_words(words),
              num_of_unique_words(words),
              average_word_length(len(text_without_spances), words_num),
              average_sentence_length_by_words(sents_num, words_num),
              average_sentence_length_by_chars(len(text_without_spances), sents_num),
              num_function_words(words)]
    for tuple in vector:
        feature_vector.append(tuple[0])
        feature_names.append(tuple[1])
    words_occurrence = occurrence_of_words(words)
    feature_vector += words_occurrence[0]
    feature_names += words_occurrence[1:4]

    return feature_vector


def get_feature_names():
    """
    :returns the name of the features that have been used in the vector
    """
    if len(feature_names) == 0:
        raise Exception("The feature vector must be calculated before get_feature_names() is called")
    return feature_names


def num_of_short_words(words_list):
    """
    :param words_list: the list of the words in the text
    :returns the ratio of the short words in the text to all the words
    """
    if not words_list:
        return 0
    short_words = [x for x in words_list if len(x) < 3]
    return len(short_words) / len(words_list), "number of short words"


def num_of_long_words(words_list):
    """
    :param words_list: the list of the words in the text
    :return: the ratio of the long words in the text to all the words
    """
    if not words_list:
        return 0
    long_words = [x for x in words_list if len(x) > 9]
    return len(long_words) / len(words_list), "number of long words"


def num_of_unique_words(words_list):
    """
    :param words_list: the list of the words in the text
    :return: the ratio of the unique words in the text to all the words
    """
    if not words_list:
        return 0
    ctr = Counter(words_list)
    count = 0
    for word, repeations in ctr.items():  # for name, age in list.items():  (for Python 3.x)
        if repeations == 1:
            count += 1
    return count / len(words_list), "number of unique words"


def average_word_length(words_len_sum, words_num):
    """
    :return: the average word length
    """
    if words_num == 0:
        return 0
    return (words_len_sum / words_num), "average word length"


def average_sentence_length_by_words(sents_num, words_num):
    """
    :param sents_num: how many sentences in the text
    :param words_num: how many words in the text
    :return: the words' num average in a sentence
    """
    if sents_num == 0:
        return 0
    return words_num / sents_num, "average sentence length by words"


def average_sentence_length_by_chars(text_len_without_signs, sents_num):
    """
    :param sents_num: how many sentences in the text
    :param text_len_without_signs: how many characters (belong only to words) in the text
    :return: the characters' num average in a sentence
    """
    if sents_num == 0:
        return 0
    return text_len_without_signs / sents_num, "average sentence length by chars"


def occurrence_of_words(words):
    """
    :param words: list that contains all the words in the text
    :returns a list that contains how many words occur once, twice and 3 times
    """
    words_set = set()
    twice_occur_set = set()
    third_occur_set = set()
    for word in words:
        if word in twice_occur_set:
            third_occur_set.add(word)
        elif word in words_set:
            twice_occur_set.add(word)
        else:
            words_set.add(word)

    unique_words = words_set - twice_occur_set
    twice_time = twice_occur_set - third_occur_set

    return [len(words_set), len(unique_words), len(twice_time)], "number of words that appear more than twice", \
           "number of words that appear twice", "number of unique words"


def num_function_words(words_list):
    """
    :param words_list: a list that contains all the words in the text
    :returns how many function words in the text
    """
    stp = nltk.corpus.stopwords.words('english')
    filtered_text = [w for w in words_list if w in stp]
    return len(filtered_text), "number of function words"
