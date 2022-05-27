
import nltk
#nltk.download()
from nltk.corpus import brown
brown.words()
tagged = brown.tagged_words(tagset='universal')
noundist = nltk.FreqDist(w2 for ((w1, t1), (w2, t2)) in
nltk.bigrams(brown.tagged_words(tagset="universal"))
if w1.lower() == "the" and t2 == "NOUN")
print(noundist.most_common(10))

