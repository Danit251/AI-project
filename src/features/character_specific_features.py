import re

special_chars = ['~', '@', '#', "$", '%', '^', '&', '*', '-', '_', '=',
                 '+', '<', '>', '|', '[', ']', '{', '}', '\\', '/']

FEATURE_NUM = 6
feature_names = []


def get_feature_vector(text):
    """
    :param text: text to vectorize
    :returns vector that represents the character features in the text
    """
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
    """
    :returns the name of the features that have been used in the vector
    """
    if len(feature_names)==0:
        return ["ratio of special chars", "ratio of letters", "ratio digit to char", "ratio space to text length",
                "ratio of spaces to white_space", "ratio tabs to white spaces"]
    return feature_names


def __num_of_chars(text):
    """
    :param text: for evaluation
    :returns how many characters in the text
    """
    return len(text)


def __num_of_alphabetic_chars(text):
    """
    :param text: for evaluation
    :return: how many alphabetic characters in the text
    """
    filtered = [c for c in text if c.isalpha()]
    return len(filtered)


def __num_of_upper_case_chars(text):
    """
    :param text: for evaluation
    :return: the number of uppercase letters in the text
    """
    filtered = [c for c in text if c.isupper()]
    return len(filtered)


def __num_of_digit(text):
    """
    :param text: for evaluation
    :return: the number of digits in the text
    """
    filtered = [c for c in text if c.isdigit()]
    return len(filtered)


def __num_of_white_space(text):
    """
    :param text: for evaluation
    :return: the number of whitespaces in the text
    """
    return len(re.findall('\s', text))


def __num_of_tab_chars(text):
    """
    :param text: for evaluation
    :return: the number of the tabs in the text
    """
    a = text.count('\t')
    return a


def __num_of_spaces(text):
    """
    :param text: for evaluation
    :return: the number of the spaces in the text
    """
    return len(re.findall(' ', text))


def ratio_of_special_chars(text):
    """
    :param text: for evaluation
    :return: the ratio of special characters (to all characters) in the text
    """
    filtered = [c for c in text if c in special_chars]
    try:
        return len(filtered) / len(text), "ratio of special chars"
    except ZeroDivisionError:
        return 1, "ratio of special chars"


def ratio_of_letters(text):
    """
    :param text: for evaluation
    :return: the ratio of letters (to all characters) in the text
    """
    try:
        return __num_of_alphabetic_chars(text) / len(text), "ratio of letters"
    except ZeroDivisionError:
        return 1, "ratio of letters"


def ratio_digit_to_char(text):
    """
    :param text: for evaluation
    :return: the ratio of digits (to all characters) in the text
    """
    try:
        return __num_of_digit(text) / len(text), "ratio digit to char"
    except ZeroDivisionError:
        return 1, "ratio digit to char"


def ratio_space_to_text_length(text):
    """
    :param text: for evaluation
    :return: the ratio of spaces (to all characters) in the text
    """
    try:
        return __num_of_spaces(text) / len(text), "ratio space to text length"
    except ZeroDivisionError:
        return 1, "ratio space to text length"


def ratio_of_spaces_to_white_space(text):
    """
    :param text: for evaluation
    :return: the ratio of spaces to whitespaces in the text
    """
    try:
        return __num_of_spaces(text) / __num_of_white_space(text), "ratio of spaces to white_space"
    except ZeroDivisionError:
        return 1, "ratio of spaces to white_space"


def ratio_tabs_to_white_spaces(text):
    """
    :param text: for evaluation
    :return: the ratio of tabs to all whitespaces in the text
    """
    try:
        return __num_of_tab_chars(text) / __num_of_white_space(text), "ratio tabs to white spaces"
    except ZeroDivisionError:
        return 1, "ratio tabs to white spaces"
