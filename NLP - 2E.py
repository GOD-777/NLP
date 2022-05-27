
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
text = nltk.word_tokenize("The night is cold, with a lot of stars in the sky and huge tress along sides of the road")
tokenized=dict(nltk.pos_tag(text))
print(tokenized)
