import nltk
nltk.download('omw-1.4')

from nltk.corpus import wordnet

syn = wordnet.synsets('hello')[0]
print("Synset name: ",syn.name())
print("\nSynset Definition: ",syn.definition())
print("\nSynset example: ",syn.examples())
synonyms=[]
antonyms=[]
for syn in wordnet.synsets("good"):
 for I in syn.lemmas():
     synonyms.append(I.name())
 if I.antonyms():
     antonyms.append(I.antonyms()[0].name())
print("\nSynset Synonyms: ",set(synonyms))
print("\nSynset Aynonyms: ",set(antonyms)) 
