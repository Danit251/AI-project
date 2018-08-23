import string
import nltk
import re

FEATURE_NUM = 43
tags_count = 0
tags_frequencies = {}
verbs_frequencies = {}

"""
The List of tags is taken from the link:
https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html 
The tagger actually uses more than that, for example: "."is tagged as "." 
"""

tags_list = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP',
             'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB',
             'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']

feature_names = []

def calculate_syntactic_feature_vector(text, author, book, filename):
    """
    :param text: text to vectorize
    :param author: whom wrote the text
    :param book: which the text is taken from
    :param filename: which the text is taken from
    :returns vector that represents the syntactic features in the text
    """
    initialize(text)
    punc_char_rat = punctuation_chars_ratio(text)
    vector = [punc_char_rat[0]]
    global feature_names
    feature_names = [punc_char_rat[1]]

    # This is done this way to make sure all the texts have the features in the this order.
    for tag in tags_list:
        res = get_pos_tag_frequency(tag)
        vector.append(res[0])
        feature_names.append(res[1])
    past_tense = past_tense_frequency()
    vector.append(past_tense[0])
    feature_names.append(past_tense[1])
    present_tense = present_tense_frequency()

    # these two don't sum up to 1 because there's another category (base form verb)
    vector.append(present_tense[0])
    feature_names.append(present_tense[1])

    avg_tree_depth = average_tree_depth(author, book, filename)
    vector.append(avg_tree_depth[0])
    feature_names.append(avg_tree_depth[1])
    return vector


def get_feature_names():
    """
    :returns the name of the features that have been used in the vector
    """
    if len(feature_names) == 0:
        names = ["punctuation chars ratio"]
        for tag in tags_list:
            names.append("frequency of " + tag)
        names += ["past tense frequency", "present tense frequency", "average tree depth"]
        return names
    return feature_names


def initialize(text):
    """
    initializes global parameters
    """
    global tagged_text
    tagged_text = pos_tag(text)
    relative_frequencies_of_tags()


def punctuation_chars_ratio(text):
    """
    :param text: for Evaluation
    :returns ratio of punctuations characters to all other characters
    """
    if len(text) == 0:
        return 0, "punctuation chars ratio"
    punctuation_count = sum([1 for char in text if char in set(string.punctuation)])
    return punctuation_count / len(text), "punctuation chars ratio"


def pos_tag(text):
    """
    :param text: for evaluation
    :returns the nltk
    """
    tokens = nltk.word_tokenize(text)
    return nltk.pos_tag(tokens)


def relative_frequencies_of_tags():
    """
    Updating relative tags found in the text in a dictionary
    """
    tags_dict = {}
    for tag in tags_list:
        tags_dict[tag] = 0
        if "VB" in tag:
            verbs_frequencies[tag] = 0
    global tags_count
    for word_tag_tuple in tagged_text:
        tag = word_tag_tuple[1]
        if tag in tags_list:
            # This is done because the tags' list doesn't actually contain all the possible tags, as explained above
            tags_count += 1
            tags_dict[tag] += 1

        if "VB" in tag:
            add_to_verb_dict(tag)
    global tags_frequencies
    tags_frequencies = tags_dict


def add_to_verb_dict(tag):
    """
    :param tag: the current tag to check
    """
    global tags_count, verbs_frequencies
    if tag in tags_list:
        # This is done because the tags' list doesn't actually contain all the possible tags, as explained above
        tags_count += 1
        verbs_frequencies[tag] += 1


def get_pos_tag_frequency(tag):
    """
    :param tag: the current tag to check
    :returns frequency for the given tag in the text
    """
    if tag not in tags_frequencies:
        return 0, "frequency of " + tag

    # This is done because the tags' list doesn't actually contain all the possible tags, as explained above
    return tags_frequencies[tag] / tags_count, "frequency of " + tag


def past_tense_frequency():
    """
    :returns: how many words are used in past tense
    """
    # This is done because the tags' list doesn't actually contain all the possible tags, as explained above
    return (verbs_frequencies["VBD"] + verbs_frequencies[
        "VBN"]) / tags_count, "past tense frequency"


def present_tense_frequency():
    """
    :returns how many words are used in present tense
    """
    # This is done because the tags' list doesn't actually contain all the possible tags, as explained above
    return (verbs_frequencies["VBG"] + verbs_frequencies["VBP"] + verbs_frequencies[
        "VBZ"]) / tags_count, "present tense frequency"


def dependency_parse(sent, parser):
    """
    :param sent: senctence to parse
    :param parser: to use to evaluate the sentence
    :returns the parsed sentence
    """
    res = parser.annotate(sent, properties={'annotators': 'parse', 'outputFormat': 'json'})
    return res['sentences'][0]['parse']


def average_tree_depth(author, book, filename):
    """
    calculates the average tree depth for every text
    :param author: whom wrote the book
    :param book: which the text is taken from
    :param filename: which the text is taken from
    """
    total_trees_depth = 0
    with open("corpus/parsed_data/" + author + "/" + book + "/" + filename, 'r', encoding='utf-8',
              errors='ignore') as file:
        parsed_text = file.read()
    parsed_sents = parsed_text.split("\n~~~~~~\n")
    for parsed_sent in parsed_sents:
        if parsed_sent and parsed_sent != "no parsing":
            total_trees_depth += find_tree_depth(parsed_sent)
    return total_trees_depth / len(parsed_sents), "average tree depth"


def find_tree_depth(tree):
    """
    Calculates the tree depth
    :param Tree: for evaluation
    """
    lines = tree.split("\n")
    depth = 0
    for line in lines:
        line_depth = re.search('\S', line).start()
        if line_depth > depth:
            depth = line_depth
    return depth / 2
