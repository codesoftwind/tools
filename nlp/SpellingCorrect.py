#-*-coding:utf-8-*-
from textblob import *

def sentenceSpellCorrect(sentence):
    '''输入：字符串
       输出：字符串'''
    return TextBlob(sentence).correct()

def wordSpellCorrect(word):
    '''输入：字符串
       输出：字符串'''
    return Word(word).spellcheck()[0][0]

def getSynonyms(word):
    '''输入：字符串
       输出：字符串的list'''
    synonyms = []
    for synset in Word(word).synsets:
        synonyms += synset.lemma_names()
    return synonyms

if __name__ == '__main__':
    sentence = "i havv goog speling"
    word = 'havv'
    print sentenceSpellCorrect(sentence)
    print wordSpellCorrect(word)
