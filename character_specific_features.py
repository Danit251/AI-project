import re
special_chars = ['~', '@', '#', "$", '%', '^', '&', '*', '-', '_', '=',
                 '+', '<', '>', '|', '[', ']', '{', '}', '\\', '/']


def num_of_chars(text):
    return len(text)


def num_of_alphabetic_chars(text):
    filtered = [c for c in text if c.isalpha()]
    return len(filtered)


def num_of_upper_case_chars(text):
    filtered = [c for c in text if c.isupper()]
    return len(filtered)


def num_of_digit(text):
    filtered = [c for c in text if c.isdigit()]
    return len(filtered)


def num_of_white_space(text):
    return len(re.findall('\s', text))


def num_of_tab_chars(text):
    a = text.count('\t')
    return a


def fraction_of_special_chars(text):
    filtered = [c for c in text if c in special_chars]
    return len(filtered)/len(text)


def fraction_of_letters(text):
    return num_of_alphabetic_chars(text)/len(text)


def ratio_digit_to_char(text):
    try:
        return num_of_alphabetic_chars(text)/num_of_digit(text)
    except ZeroDivisionError:
        return 1


def ratio_space_to_word_length(text):
    return num_of_spaces(text)/len(text)


def num_of_spaces(text):
    return len(re.findall(' ', text))


def ratio_of_spaces_to_white_space(text):
    return num_of_spaces(text)/num_of_white_space(text)


def ratio_tabs_to_white_spaces(text):
    return num_of_tab_chars(text)/num_of_white_space(text)
