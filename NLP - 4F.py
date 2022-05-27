
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
import spacy
from keras.preprocessing.text import text_to_word_sequence
from gensim.utils import tokenize
text = """Founded in 2002, SpaceX’s mission is to enable humans to become a spacefaring civilization and a multi-planet species by building a self-sustaining city on Mars. In 2008, SpaceX’s Falcon 1 became the first privately developed
liquid-fuel launch vehicle to orbit the Earth."""
print("\n\nGenism Tokenization:",list(tokenize(text)))
