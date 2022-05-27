
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
for syn in wn.synsets("good"):
 print(syn.lemmas())
machine_that_prints = wn.synset('printer.n.03')
print("hyponyms: ",sorted([lemma.name() for synset in machine_that_prints.hyponyms for lemma in synsets.lemmas()]))
print("hypernyms: ",[lemma.name() for synset in machine_that_prints.hypernyms
 for lemma in synsets.lemmas()])
print("Entailments: ",wn.synset('eat.v.01').entailments())

