import os

from nltk.corpus import PlaintextCorpusReader

data_set = 'gutenberg'
# data_set = 'C50'

for filename in os.listdir('raw_data'):
    author, book_name = filename.split('-')
    if book_name:
        directory = '{}/data/{}/{}'.format(data_set, author.lower(), filename)
    else:
        directory = '{}/data/{}'.format(data_set, author.lower())
    if not os.path.exists(directory):
        os.makedirs(directory)
    f = open("{}/Metadata".format(directory), "w+")
    corpus = PlaintextCorpusReader("", filename)
    # Counts the number of chapters
    count = 0

    for sen in corpus.sents('raw_data/{}'.format(filename)):

        # Opens new file to every chapter
        if "chapter" in [w.lower() for w in sen]:
            f.close()
            f = open("{}/{}_{}.txt".format(directory, filename, str(count)), "w+")
            count += 1
        else:
            s = " ".join(sen) + " "
            # Encoding latin letters
            # e = s.encode('utf-8', errors='replace')
            f.write(s)
    f.close()