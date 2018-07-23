import string
import nltk

nltk.download('stopwords')

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
        for sign in set(string.punctuation):
            word = word.replace(sign+" ", "")
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


def occurance_of_words(text):
    words_set = set()
    twice_occur_set = set()
    third_occur_set = set()
    words = text.split(" ")
    for word in words:
        if word in set(string.punctuation):
            continue
        for sign in set(string.punctuation):
            word = word.replace(sign+" ", "")

        if word in twice_occur_set:
            third_occur_set.add(word)
        elif word in words_set:
            twice_occur_set.add(word)
        else:
            words_set.add(word)


    unique_words = words_set - twice_occur_set
    twice_time = twice_occur_set - third_occur_set

    return [len(words_set), len(unique_words), len(twice_time)]


def num_function_words(text):
    stp = nltk.corpus.stopwords.words('english')
    # filtered_text = [w for w in text if w in stp]
    print(stp)



with open("corpus/data/austen/austen-sense/austen-sense_8.txt", 'r') as file:
    text = file.read()

text = "this is a test sentence that is hopefully long enough to be helpful. a a"

# print(calculate_words_feature_vector(text))
# print(occurance_of_words(text))
num_function_words(text)