from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
from pprint import pprint

dict = {}


def collect(j):
    global dict
    file = open('D:\jatan-ir\docs\doc' + str(j) + '.txt', encoding='utf8')
    read = file.read()
    file.seek(0)

    line = 1
    for word in read:
        if word == '\n':
            line += 1
    print("Number of lines in file is: ", line)

    # create a list to
    # store each line as
    # an element of list
    array = []
    for i in range(line):
        array.append(file.readline())

    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
    for ele in read:
        if ele in punc:
            read = read.replace(ele, " ")

    # to maintain uniformity
    read = read.lower()

    for i in range(1):
        # this will convert
        # the word into tokens
        text_tokens = word_tokenize(read)

    tokens_without_sw = [
        word for word in text_tokens if not word in stopwords.words()]

    # to obtain the
    # number of lines

    for i in range(line):
        check = array[i].lower()
        for item in tokens_without_sw:
            if item in check:
                if item not in dict:
                    dict[item] = []

                if item in dict:
                    if i + 1 not in dict[item]:
                        m = []
                        m.append(j)
                        m.append(i + 1)
                        if (m not in dict[item]):
                            dict[item].append(m)


for i in range(0, 3):
    collect(i + 1)

pprint(dict)

s = input("Enter search query (doc no,line no):  ")
# print(dict.keys())
# for i in range(len(dict)):
m1 = []
if s in dict:
    print(dict.get(s))
else:
    print("QUERY NOT FOUND")