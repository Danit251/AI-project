import string
import nltk

nltk.download('stopwords')

def calculate_words_feature_vector(text):
    # parse_text(text)
    # vector = [num_of_short_words()]
    # vector.append(average_word_length())
    # vector.append(average_sentence_length_by_words(text))
    # vector.append(average_sentence_length_by_chars())
    # print(text)
    text_without_punc = text
    signs = set(string.punctuation)
    signs.remove('.')
    for sign in signs:
        text_without_punc =  text_without_punc.replace(sign, "")
        # text_without_punc =  text_without_punc.replace(" " + sign + " ", "")
        # text_without_punc =  text_without_punc.replace(" " + sign, "")

    text_without_dot =  text_without_punc.replace('.', "")
    words = text_without_dot.split(" ")
    # words_num = len(words)
    # sents_num = text_without_punc.count('.')
    # vector = [words_num + sents_num]

    vector = [average_sentence_length_by_words(text_without_punc, words)]
    # , average_sentence_length_by_chars(text_without_punc)]
    # vector = [num_of_short_words(words), average_word_length(words)]
    # vector = [num_function_words(text)]
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



def num_of_short_words(words):
    if not words:
        return 0
    short_words = [x for x in words if len(x) < 3]
    return len(short_words) / len(words)


def average_word_length(words):
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)


def average_sentence_length_by_words(text, words):
    # sentences = text.split(" . ")
    # len_by_words = 0
    # global len_by_chars, num_sents
    # len_by_chars = 0
    # num_sents = 0
    # for sen in sentences:
    #     for sign in set(string.punctuation):
    #         sen = sen.replace(sign+" ", "")
    #     if sen:
    #         num_sents += 1
    #         words_in_sen = sen.split(' ')
    #         len_by_words += len(words_in_sen)
    #         len_by_chars += len(sen)

    # text_without_punc = text
    # # signs = set(string.punctuation)
    # # signs.remove('.')
    # # for sign in signs:
    # #     text_without_punc =  text_without_punc.replace(sign, "")

    len_by_words = len(words)

    global sents_num
    sents_num = text.count('.')

    if sents_num == 0:
        return 0
    return len_by_words/sents_num

def average_sentence_length_by_chars(text):
    text_without_punc = text
    text_without_punc =  text_without_punc.replace(' ', "")
    len_by_chars = len(text_without_punc)
    if sents_num == 0:
        return 0
    return len_by_chars/sents_num


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
    words = text.split(" ")
    filtered_text = set(stp) & set(words)
    # filtered_text = [w for w in words if w in stp]
    # print(filtered_text)
    return len(filtered_text)


# with open("corpus/data/austen/austen-sense/austen-sense_8.txt", 'r') as file:
#     text = file.read()

# text = "this is a test sentence that is hopefully long enough to be helpful. a a"

# print(calculate_words_feature_vector(text))
# print(occurance_of_words(text))
# num_function_words(text)