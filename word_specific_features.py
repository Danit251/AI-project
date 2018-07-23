import string


def calculate_words_feature_vector(text):
    parse_text(text)
    vector = [num_of_short_words()]
    vector.append(average_word_length())
    vector.append(average_sentence_length_by_words(text))
    vector.append(average_sentence_length_by_chars())
    return vector


def parse_text(text):
    global short_words_count, words, total_words_length
    words = text.split(" ")
    short_words_count = 0
    total_words_length = 0
    for word in words:
        if word in set(string.punctuation):
            continue
        total_words_length += len(word)
        if len(word) < 3:
            short_words_count += 1



def num_of_short_words():
    if not words:
        return 0
    return short_words_count / len(words)


def average_word_length():
    if not words:
        return 0
    return total_words_length / len(words)


def average_sentence_length_by_words(text):
    sentences = text.split(" . ")
    len_by_words = 0
    global len_by_chars, num_sents
    len_by_chars = 0
    num_sents = 0
    for sen in sentences:
        for sign in set(string.punctuation):
            sen = sen.replace(sign+" ", "")
        if sen:
            num_sents += 1
            words_in_sen = sen.split(' ')
            len_by_words += len(words_in_sen)
            len_by_chars += len(sen)

    return len_by_words/num_sents


def average_sentence_length_by_chars():
    return len_by_chars/num_sents





with open("corpus/data/austen/austen-sense/austen-sense_8.txt", 'r') as file:
    text = file.read()

# text = "this is a test sentence that is hopefully long enough to be helpful."

print(calculate_words_feature_vector(text))