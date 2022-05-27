
from nltk.corpus import PlaintextCorpusReader
corpus_root = 'NLPMyCorpus-2B/'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
print(wordlists.fileids())
files=['1.txt', '2.txt']
filename=0
for text in files:
    filename+=1
with open(corpus_root+str(filename)+'.txt','r') as fout:
    print("\n",fout.read(), text)
