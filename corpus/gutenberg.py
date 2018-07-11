from nltk.corpus import gutenberg
from nltk.corpus import PlaintextCorpusReader

# ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']

f = open("data/Melville-Romance/Metadata", "w+")

n = gutenberg.fileids()
# print(n)
corpus = PlaintextCorpusReader("", 'Melville-Romance')
count = 0
for sen in corpus.sents("Melville-Romance"):
    # if 'Book' in sen:
    # print(sen)
    if "CHAPTER" in sen:
        f.close()
        f = open("data/Melville-Romance/Melville-Romance_" + str(count) + ".txt", "w+")
        count += 1
    else:
        f.write(" ".join(sen) + " ")
f.close()

# austin_corpus = PlaintextCorpusReader("data/austen-persuasion", '.*\.txt')
# austin_corpus = PlaintextCorpusReader("", 'Melville-Romance')
# names = austin_corpus.fileids()
# print(names)
# for name in names:
#     print(name)
#     for sen in austin_corpus.sents(name):
#         print(sen)
