
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
lemmatizer = WordNetLemmatizer()
sentence = "He makes a very delicious meal. It costs nothing to be good"
words = word_tokenize(sentence)
for w in words:
 print(w, " ==>: ", lemmatizer.lemmatize(w))
