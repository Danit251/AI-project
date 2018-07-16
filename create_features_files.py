"""
    This file generates training_examples.txt and test_examples.txt
    for the texts in corpus/training and corpus/test
    using the features in character_specific_features.py
"""

import os
import character_specific_features as feature_extract


def create_examples(corpus_dir, features_file):
    for author_dir in os.listdir(corpus_dir):
        for book_dir in os.listdir(corpus_dir + "/" + author_dir):
            for file_location in os.listdir(corpus_dir + "/" + author_dir + "/" + book_dir):
                file = open(corpus_dir + "/" + author_dir + "/" + book_dir + "/" + file_location, "w+")
                text = file.read()

                features_arr = []

                # to set features
                if feature_extract.ratio_space_to_word_length(text) > 0.5:
                    features_arr.append("1")
                else:
                    features_arr.append("0")

                features_arr.append(author_dir)

                features_vec = ' '.join(features_arr)
                features_file.write(features_vec + "\n")


corpus_dir = ["corpus/training", "corpus/test"]
features_dir = ["features files/training_examples.txt", "features files/test_examples.txt"]

for i in range(2):
    features_file = open(features_dir[i], 'w')
    create_examples(corpus_dir[i], features_file)
    features_file.close()

# features_file = open("features files/tagged_examples.txt", 'w')
