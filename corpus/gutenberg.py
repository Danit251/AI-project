from nltk.corpus import gutenberg
from nltk.corpus import PlaintextCorpusReader
import sys
# import nltk
# nltk.download()
# ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']
# print("St?cker".encode(sys.stdout.encoding, errors='replace'))
# print(u"St?cker")
f = open("data/bronte/Bronte-Villette/Metadata", "w+")

n = gutenberg.fileids()
# print(n)
corpus = PlaintextCorpusReader("", 'Bronte-Villette')
count = 0
for sen in corpus.sents("Bronte-Villette"):
    # if 'Book' in sen:
    # print(sen)
    if "Chapter" in sen:
        f.close()
        f = open("data/bronte/Bronte-Villette/Bronte-Villette_" + str(count) + ".txt", "w+")
        count += 1
    else:
        s = " ".join(sen) + " "
        # e = s.encode('utf-8', errors='replace')
        # print(s)
        f.write(s)
f.close()

# austin_corpus = PlaintextCorpusReader("data/austen-persuasion", '.*\.txt')
# austin_corpus = PlaintextCorpusReader("", 'Melville-Romance')
# names = austin_corpus.fileids()
# print(names)
# for name in names:
#     print(name)
#     for sen in austin_corpus.sents(name):
#         print(sen)
