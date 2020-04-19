import pyspelling
from spellchecker import SpellChecker
from nltk.tokenize import TweetTokenizer

token = TweetTokenizer()
s0 = "This is a cooool #dummysmiley: :-) :-P <3 and some arrows < > -> <--"
token.tokenize(s0)
spell = SpellChecker(language = "en", case_sensitive = False)
misspelled1 = token.tokenize(s0)
for word in misspelled1:
    if( not word.isalpha()):
        print(word)
        misspelled1.remove(word)
print(len(misspelled1))
for word in misspelled1:
    if( not word.isalpha()):
        print(word)
        misspelled1.remove(word)
print(len(misspelled1))
for word in misspelled1:
    if( not word.isalpha()):
        print(word)
        misspelled1.remove(word)
print(len(misspelled1))
for word in misspelled1:
    if( not word.isalpha()):
        print(word)
        misspelled1.remove(word)
print(len(misspelled1))        
# for word in misspelled:
#     # Get the one `most likely` answer
#     if((spell.correction(word))):
#       misspelled1.remove(word)
#       print(word)

#     # Get a list of `likely` options
#     # print(spell.candidates(word))


a = ['---']
print(misspelled1)
# print(a.isalpha())
misspelled = spell.unknown(misspelled1)


for word in misspelled:
    # Get the one `most likely` answer
    if((spell.correction(word))):
      misspelled1.remove(word)
      print(word)

    # Get a list of `likely` options
    # print(spell.candidates(word))
      
print(misspelled1)