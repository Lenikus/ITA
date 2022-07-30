import re
#import nltk
import num2words
#import pymorphy2
from nltk import word_tokenize, wordpunct_tokenize
from nltk.corpus import stopwords
from pymorphy2 import MorphAnalyzer
from nltk.stem import SnowballStemmer

morph = MorphAnalyzer()
stemmer = SnowballStemmer('russian')


def make_default_stopwords():
    stopWordsRDefault = stopwords.words("russian")
    stopWordsEDefault = stopwords.words("english")
    with open("default_stopwords.txt", "w") as file:
        for line in stopWordsRDefault:
            file.write(line + '\n')
        for line in stopWordsEDefault:
            file.write(line + '\n')


def normalize_item(item):
    item = item.lower()
    item = morph.normal_forms(item)[0]
    item = stemmer.stem(item)
    return item


def normalize_list(items):
    for i in range(len(items)):
        item = wordpunct_tokenize(items[i])
        #lexem = lexems[i].split()
        for j in range(len(item)):
            item[j] = normalize_item(item[j])
            #item[j] = item[j].lower()
            #item[j] = morph.normal_forms(item[j])[0]
            #item[j] = stemmer.stem(item[j])
        items[i] = ' '.join(i for i in item)
    return items


def text_processing(txt, lang):
    # пунктуация зависит от language!!!!!!!!!!!!!!!!!!!!!! // /* */
    # txt = re.sub(r'[^\w\s][.,]',' ', txt, flags = re.UNICODE)
    if txt.endswith('?'):
        if not txt.endswith(':?'):
            txt = txt[:-1]
    token = wordpunct_tokenize(txt)
    #for i in range(len(token)):
    #    if token[i].isdigit():
    #        token[i] = num2words(token[i], lang="russian")
    for i in range(len(token)):
        token[i] = token[i].lower()
        token[i] = morph.normal_forms(token[i])[0]
        token[i] = stemmer.stem(token[i])
    for i in token:
        if i in lang.stopwords: #and i not in lang.lexems:
            token.remove(i)
    txt = ' '.join(i for i in token)
    return txt
