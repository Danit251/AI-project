import types
import character_specific_features
import os

features_modules = [character_specific_features]


def create_features_vector(text, label):
    """
    Create a feature vector for the given text over all the public functions in all modules.
    :param text: text to vectorize
    :param label: the label of the text (mainly the author)
    :return: the vector
    """
    feature_vector = []
    features_funcs = []
    for module in features_modules:
        # list of all public functions
        features_funcs += [getattr(module, a) for a in dir(module)
               if isinstance(getattr(module, a), types.FunctionType) and not a.startswith('__')]
    for f in features_funcs:
        feature_vector.append(f(text))
    return [feature_vector, label]


def create_corpus_vector():
    """
    Iterate over all authors and their books  and create a vector for each chapter
    :return: vectors with corresponding features values.
    """
    vectors = []
    for author in os.listdir("corpus/data"):
        for book in os.listdir("corpus/data/" + author):
            for filename in os.listdir("corpus/data/" + author + "/" + book):
                if filename.endswith(".txt"):
                    with open("corpus/data/" + author + "/" + book + "/" + filename, 'r') as file:
                        text = file.read()
                        vectors.append(create_features_vector(text, author))
    return vectors



example_text = "wow"
print(create_features_vector(example_text, 'Roi Shtivi'))


print(create_corpus_vector())