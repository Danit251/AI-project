from nltk.corpus import gutenberg
from nltk.corpus import PlaintextCorpusReader

# ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt', 'bible-kjv.txt', 'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt', 'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt', 'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt', 'milton-paradise.txt', 'shakespeare-caesar.txt', 'shakespeare-hamlet.txt', 'shakespeare-macbeth.txt', 'whitman-leaves.txt']

f = open("Metadata", "w+")

n = gutenberg.fileids()
# print(n)
count = 0
for sen in gutenberg.sents("austen-emma.txt"):
    if "CHAPTER" in sen:
        f.close()
        f = open("austen-emma_" + str(count) + ".txt", "w+")
        count += 1
    else:
        f.write(" ".join(sen) + " ")
f.close()

austin_corpus = PlaintextCorpusReader("", '.*\.txt')
names = austin_corpus.fileids()
# print(names)
for name in names:
    print(name)
    for sen in austin_corpus.sents(name):
        print(sen)
