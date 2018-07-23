import re
special_chars = ['~', '@', '#', "$", '%', '^', '&', '*', '-', '_', '=',
                 '+', '<', '>', '|', '[', ']', '{', '}', '\\', '/']


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
        return len(filtered)/len(text)
    except ZeroDivisionError:
        return 1


def ratio_of_letters(text):
    try:
        return __num_of_alphabetic_chars(text)/len(text)
    except ZeroDivisionError:
        return 1


def ratio_digit_to_char(text):
    try:
        return __num_of_digit(text)/len(text)
    except ZeroDivisionError:
        return 1


def ratio_space_to_word_length(text):
    try:
        return __num_of_spaces(text)/len(text)
    except ZeroDivisionError:
        return 1


def ratio_of_spaces_to_white_space(text):
    try:
        return __num_of_spaces(text)/__num_of_white_space(text)
    except ZeroDivisionError:
        return 1


def ratio_tabs_to_white_spaces(text):
    try:
        return __num_of_tab_chars(text)/__num_of_white_space(text)
    except ZeroDivisionError:
        return 1
