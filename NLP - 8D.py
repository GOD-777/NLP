
import nltk
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
lancaster = LancasterStemmer()
terms = ["enjoy", "enjoying", "enjoyed", "enjoyable", "enjoyment", "enjoyful"]
print("\n1. Performing lancaster stemming on the words")
for each_term in terms:
 print(lancaster.stem(each_term))
sentence = " Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better"
print("\n2. Performing lancaster stemming on a sentence")
words = word_tokenize(sentence, language = 'english')
for each_word in words:
    print(lancaster.stem(each_word))
print("\n3. Performing lancaster stemming on a text file - one sentence at a time")
word_file = open("NLP - 8D.txt")
my_lines_list = word_file.readlines()
words = word_tokenize(my_lines_list[0], language = 'english')
for each_word in words:
 print(lancaster.stem(each_word))

