import types
import character_specific_features
import syntactic_features
import word_specific_features
import os
import numpy as np
import random
import util


def create_features_vector(text, label, author, book, filename, features_mask):
    """
    Create a feature vector for the given text over all the public functions in all modules.
    :param text: text to vectorize
    :param label: the label of the text (mainly the author)
    :return: the vector
    """
    feature_vector = []
    if features_mask[0]:
        feature_vector += character_specific_features.get_feature_vector(text)
    if features_mask[1]:
        feature_vector += syntactic_features.calculate_syntactic_feature_vector(text, author, book, filename)
    if features_mask[2]:
        feature_vector += word_specific_features.calculate_words_feature_vector(text)
    return [feature_vector, label, book]


def create_corpus_vector(authors_num=5, features_mask=[1] * 3):
    """
    Iterate over all authors and their books  and create a vector for each chapter
    :return: vectors with corresponding features values.
    """
    vectors = []
    for author in os.listdir("corpus/data")[:authors_num]:
        for book in os.listdir("corpus/data/" + author):
            for filename in os.listdir("corpus/data/" + author + "/" + book):
                if filename.endswith(".txt"):
                    with open("corpus/data/" + author + "/" + book + "/" + filename, 'r', encoding='utf-8', errors='ignore') as file:
                        text = file.read()
                        vectors.append(create_features_vector(text, author, author, book, filename, features_mask))
    return np.asarray(vectors)


def split_train_test(data):
    test_data = []
    training_data = []
    for author in os.listdir("corpus/data"):
        if author.startswith("."):
            continue
        num_of_books = len(os.listdir("corpus/data/" + author))
        test_book_index = random.randint(0, num_of_books - 1)
        while os.listdir("corpus/data/" + author)[test_book_index].startswith("."):
            test_book_index = random.randint(0, num_of_books - 1)  # TODO delete. This is needed only on mac
        test_book = os.listdir("corpus/data/" + author)[test_book_index]
        print("test: ", test_book)
        for item in data:
            if item[2] == test_book:
                test_data.append(item)
            else:
                training_data.append(item)
    return np.asarray(training_data), np.asarray(test_data)
