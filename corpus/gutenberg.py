from nltk.corpus import PlaintextCorpusReader

f = open("data/stoker/Stoker-Dracula/Metadata", "w+")

corpus = PlaintextCorpusReader("", 'Stoker-Dracula')

# Counts the number of chapters
count = 0

for sen in corpus.sents("Stoker-Dracula"):

    # Opens new file to every chapter
    if "CHAPTER" in sen:
        f.close()
        f = open("data/stoker/Stoker-Dracula/Stoker-Dracula_" + str(count) + ".txt", "w+")
        count += 1
    else:
        s = " ".join(sen) + " "
        # Encoding latin letters
        # e = s.encode('utf-8', errors='replace')
        f.write(s)
f.close()