import string
import nltk
import re
# from nltk.parse.stanford import StanfordDependencyParser
# from stanfordcorenlp import StanfordCoreNLP
from pycorenlp import StanfordCoreNLP


# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')

tags_count = 0
tags_frequencies = {}
verbs_frequencies = {}
tags_list = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP',
             'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB',
             'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']
# the list is from here: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
# the tagger actually uses more than that, for example "." is tagged as ".". TODO: try to find the full list of possible tags


def calculate_syntactic_feature_vector(text, author, book, filename):
    # print("init")
    initialize(text)
    # print("punctuation_chars_ratio")
    vector = [punctuation_chars_ratio(text)]
    # print("tags")
    for tag in tags_list:  # this has to be done this way because we want the vector to contain the
        # same features in the same order for all the texts (meaning we can't use a data structure
        # that has no defined order and we can't look only at the tags that appear in this specific text)
        vector.append(get_pos_tag_frequency(tag))
    vector.append(past_tense_frequency())
    vector.append(present_tense_frequency())  # these two don't sum up to 1 because there's another
    # category (base form verb)
    vector.append(average_tree_depth(author, book, filename))
    return vector


def initialize(text):
    global tagged_text
    tagged_text = pos_tag(text)
    relative_frequencies_of_tags()


def punctuation_chars_ratio(text):
    if len(text) == 0:
        return 0
    punctuation_count = sum([1 for char in text if char in set(string.punctuation)])
    return punctuation_count / len(text)


def pos_tag(text):
    tokens = nltk.word_tokenize(text)
    return nltk.pos_tag(tokens)
    # I tried to use coreNLPPOSTagger: https://cindyxiaoxiaoli.wordpress.com/2017/04/10/how-to-use-stanford-corenlp-in-python/
    # but it failed and I couldn't solve it. Anyway, I think the nltk tagger should be fine too.
    # another option is to use this:
    # tagger = StanfordPOSTagger('/Users/nogastern/Desktop/AI/project/AI-project/stanford-postagger-full-2018-02-27/models/english-bidirectional-distsim.tagger', path_to_jar= '/Users/nogastern/Desktop/AI/project/AI-project/stanford-postagger-full-2018-02-27/stanford-postagger.jar')
    # but then we get a comment saying we should use the CoreNLPPOSTagger, which is the one that didn't work
    # (also, I used the path in my computer, this will not work on a computer in the aquarium)


def relative_frequencies_of_tags():
    tags_dict = {}
    for tag in tags_list:
        tags_dict[tag] = 0
        if "VB" in tag:
            verbs_frequencies[tag] = 0
    global tags_count
    for word_tag_tuple in tagged_text:
        tag = word_tag_tuple[1]
        if tag in tags_list:
            tags_count += 1 # this is here because the tags list doesn't actually contain all the possible
            # tags, as explained above
            tags_dict[tag] += 1
        if "VB" in tag:
            add_to_verb_dict(tag)
    global tags_frequencies
    tags_frequencies = tags_dict


def add_to_verb_dict(tag):
    global tags_count, verbs_frequencies
    if tag in tags_list:
        tags_count += 1 # this is here because the tags list doesn't actually contain all the possible
        # tags, as explained above
        verbs_frequencies[tag] += 1


def get_pos_tag_frequency(tag):
    if tag not in tags_frequencies:
        return 0
    return tags_frequencies[tag] / tags_count  # the tag_count is here (instead of just using the length of the sentence)
    #  because the tags list doesn't actually contain all the possible tags, as explained above


def past_tense_frequency():
    return (verbs_frequencies["VBD"] + verbs_frequencies["VBN"]) / tags_count  # the tag_count is here (instead of just using the length of the sentence)
    #  because the tags list doesn't actually contain all the possible tags, as explained above


def present_tense_frequency():
    return (verbs_frequencies["VBG"] + verbs_frequencies["VBP"] + verbs_frequencies["VBZ"]) / tags_count
    # the tag_count is here (instead of just using the length of the sentence)
    #  because the tags list doesn't actually contain all the possible tags, as explained above


def dependency_parse(sent, parser):
    res = parser.annotate(sent, properties={'annotators':'parse', 'outputFormat': 'json'})
    return res['sentences'][0]['parse']


def average_tree_depth(author, book, filename):
    total_trees_depth = 0
    with open("corpus/parsed_data/"+author+"/"+book+"/"+filename, 'r') as file:
        parsed_text = file.read()
    parsed_sents = parsed_text.split("\n~~~~~~\n")
    for parsed_sent in parsed_sents:
        if parsed_sent and parsed_sent != "no parsing":
            total_trees_depth += find_tree_depth(parsed_sent)
    return total_trees_depth / len(parsed_sents)


def find_tree_depth(tree):
    lines = tree.split("\n")
    depth = 0
    for line in lines:
        line_depth = re.search('\S', line).start()
        if line_depth > depth:
            depth = line_depth
    return depth/2


# with open("corpus/data/austen/austen-sense/austen-sense_8.txt", 'r') as file:
#     text = file.read()

# text = "this is a test sentence that is hopefully long enough to be helpful . This is another sentence, just to make it longer and more interesting"
# print(calculate_syntactic_feature_vector(text, "austen", "austen-sense", "austen-sense_8.txt"))
# print(average_tree_depth(text, ""))
