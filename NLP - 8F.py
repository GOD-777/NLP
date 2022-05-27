
import nltk
from nltk.stem import RegexpStemmer
# Defining the stemmer
regexp = RegexpStemmer('ing$|s$|e$|able$|ment$|less$|ly$', min=4)
# Performing stemming one word
print("\n1. Performing regexp stemming on one word at a time")
print(regexp.stem('cars'))
print(regexp.stem('bee'))
terms = ["nlp", "stemming", "mentally", "ease","rockstar", "frictionless", "management","flowers", "advisable"]
# Performing stemming using lancaster stemmer on words
print("\n2. Performing regexp stemming on a list of words")
for each_term in terms:
 print(regexp.stem(each_term))
