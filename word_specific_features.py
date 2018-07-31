import string
import nltk

nltk.download('stopwords')


def calculate_words_feature_vector(text):
    signs = set(string.punctuation)
    signs.remove('.')

    text_without_punc = text
    for sign in signs:
        text_without_punc = text_without_punc.replace(sign, "")
        # text_without_punc =  text_without_punc.replace(" " + sign + " ", "")
        # text_without_punc =  text_without_punc.replace(" " + sign, "")

    text_without_dot = text_without_punc.replace(" .", "")
    text_without_spances = text_without_dot.replace(' ', "")
    words = text_without_dot.split(" ")
    words_num = len(words)
    sents_num = text_without_punc.count(" .")

    vector = [num_of_short_words(words), average_word_length(len(text_without_spances), words_num),
              average_sentence_length_by_words(sents_num, words_num),
              average_sentence_length_by_chars(len(text_without_spances), sents_num), num_function_words(words)]
    # vector += occurance_of_words(words)
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
            word = word.replace(sign + " ", "")
        total_words_length += len(word)
        if len(word) < 3:
            short_words_count += 1


def num_of_short_words(words_list):
    if not words_list:
        return 0
    short_words = [x for x in words_list if len(x) < 3]
    return len(short_words) / len(words_list)


def average_word_length(words_len_sum, words_num):
    # if not words:
    #     return 0
    # return sum(len(word) for word in words) / len(words)
    if words_num == 0:
        return 0
    return words_len_sum / words_num


def average_sentence_length_by_words(sents_num, words_num):
    if sents_num == 0:
        return 0
    return words_num / sents_num


def average_sentence_length_by_chars(text_len_without_signs, sents_num):
    if sents_num == 0:
        return 0
    return text_len_without_signs / sents_num


def occurance_of_words(words):
    words_set = set()
    twice_occur_set = set()
    third_occur_set = set()
    # words = text.split(" ")
    for word in words:
        # if word in set(string.punctuation):
        #     continue
        # for sign in set(string.punctuation):
        #     word = word.replace(sign + " ", "")

        if word in twice_occur_set:
            third_occur_set.add(word)
        elif word in words_set:
            twice_occur_set.add(word)
        else:
            words_set.add(word)

    unique_words = words_set - twice_occur_set
    twice_time = twice_occur_set - third_occur_set

    return [len(words_set), len(unique_words), len(twice_time)]


def num_function_words(words_list):
    stp = nltk.corpus.stopwords.words('english')
    # words = text.split(" ")
    # filtered_text = set(stp) & set(words)
    filtered_text = [w for w in words_list if w in stp]
    # print(filtered_text)
    return len(filtered_text)

# with open("corpus/data/austen/austen-sense/austen-sense_8.txt", 'r') as file:
#     text = file.read()

# text = "this is a test sentence that is hopefully long enough to be helpful. a a"

# print(calculate_words_feature_vector(text))
# print(occurance_of_words(text))
# num_function_words(text)
