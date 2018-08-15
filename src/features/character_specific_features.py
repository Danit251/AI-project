import re
special_chars = ['~', '@', '#', "$", '%', '^', '&', '*', '-', '_', '=',
                 '+', '<', '>', '|', '[', ']', '{', '}', '\\', '/']


def get_feature_vector(text):
    special_chars = ratio_of_special_chars(text)
    letters = ratio_of_letters(text)
    digit_to_char = ratio_digit_to_char(text)
    space_to_text_length = ratio_space_to_text_length(text)
    spaces_to_white_space = ratio_of_spaces_to_white_space(text)
    tabs_to_white_spaces = ratio_tabs_to_white_spaces(text)
    global feature_names
    feature_names = [special_chars[1],
     letters[1],
     digit_to_char[1],
     space_to_text_length[1],
     spaces_to_white_space[1],
     tabs_to_white_spaces[1]]
    return [special_chars[0],
            letters[0],
            digit_to_char[0],
            space_to_text_length[0],
            spaces_to_white_space[0],
            tabs_to_white_spaces[0]
            ]


def get_feature_names():
    if len(feature_names) == 0:
        raise Exception("The feature vector must be calculated before get_feature_names() is called")
    return feature_names

def __num_of_chars(text):
    return len(text)


def __num_of_alphabetic_chars(text):
    filtered = [c for c in text if c.isalpha()]
    return len(filtered)


def __num_of_upper_case_chars(text):
    filtered = [c for c in text if c.isupper()]
    return len(filtered)


def __num_of_digit(text):
    filtered = [c for c in text if c.isdigit()]
    return len(filtered)


def __num_of_white_space(text):
    return len(re.findall('\s', text))


def __num_of_tab_chars(text):
    a = text.count('\t')
    return a


def __num_of_spaces(text):
    return len(re.findall(' ', text))


def ratio_of_special_chars(text):
    filtered = [c for c in text if c in special_chars]
    try:
        return len(filtered)/len(text), "ratio of special chars"
    except ZeroDivisionError:
        return 1, "ratio of special chars"


def ratio_of_letters(text):
    try:
        return __num_of_alphabetic_chars(text)/len(text), "ratio of letters"
    except ZeroDivisionError:
        return 1, "ratio of letters"


def ratio_digit_to_char(text):
    try:
        return __num_of_digit(text)/len(text), "ratio digit to char"
    except ZeroDivisionError:
        return 1, "ratio digit to char"


def ratio_space_to_text_length(text):
    try:
        return __num_of_spaces(text)/len(text), "ratio space to text length"
    except ZeroDivisionError:
        return 1, "ratio space to text length"


def ratio_of_spaces_to_white_space(text):
    try:
        return __num_of_spaces(text)/__num_of_white_space(text), "ratio of spaces to white_space"
    except ZeroDivisionError:
        return 1, "ratio of spaces to white_space"


def ratio_tabs_to_white_spaces(text):
    try:
        return __num_of_tab_chars(text)/__num_of_white_space(text), "ratio tabs to white spaces"
    except ZeroDivisionError:
        return 1, "ratio tabs to white spaces"
