
from nltk.corpus import wordnet
synonyms = []
antonyms = []
for syn in wordnet.synsets("active"):
 for I in syn.lemmas():
     synonyms.append(I.name())
 if I.antonyms():
     antonyms.append(I.antonyms()[0].name())
print("\nSynset Synonyms : ",set(synonyms))
print("\nSynset Antonyms : ",set(antonyms))
