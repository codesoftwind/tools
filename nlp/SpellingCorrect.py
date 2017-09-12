from textblob import *

def sentenceSpellCorrect(sentence):
    return TextBlob(sentence).correct()

def wordSpellCorrect(word):
    return Word(word).spellcheck()[0][0]

if __name__ == '__main__':
    sentence = "i havv goog speling"
    word = 'havv'
    print sentenceSpellCorrect(sentence)
    print wordSpellCorrect(word)