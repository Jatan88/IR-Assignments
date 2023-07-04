import glob
import math
import re
import sys
from collections import defaultdict
from functools import reduce

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tkinter import *
from tkinter import filedialog

import nltk
nltk.download('stopwords')
nltk.download('punkt')

STOPWORDS = set(stopwords.words("english"))
CORPUS = "docs/*"
document_filenames = dict()
N = 0
vocabulary = set()
postings = defaultdict(dict)
document_frequency = defaultdict(int)
length = defaultdict(float)


def main():
    get_corpus()
    initialize_terms_and_postings()
    initialize_document_frequencies()
    initialize_lengths()
    while True:
        scores = do_search()
        print_scores(scores)


def get_corpus():
    global document_filenames,N
    documents = glob.glob(CORPUS)
    N = len(documents)
    document_filenames = dict(zip(range(N), documents))


def initialize_terms_and_postings():
    global vocabulary, postings
    for id in document_filenames:
        with open(document_filenames[id], "r", encoding="utf-8") as f:
          document = f.read()
        document = remove_special_characters(document)
        document = remove_digits(document)
        terms = tokenize(document)
        unique_terms = set(terms)
        vocabulary = vocabulary.union(unique_terms)
        for term in unique_terms:
            postings[term][id] = terms.count(term)


def tokenize(document):
    terms = word_tokenize(document)
    terms = [term.lower() for term in terms if term not in STOPWORDS]

    return terms


def initialize_document_frequencies():
    global document_frequency
    for term in vocabulary:
        document_frequency[term] = len(postings[term])


def initialize_lengths():
    global length
    for id in document_filenames:
        l = 0
        for term in vocabulary:
            l += term_frequency(term, id) ** 2
        length[id] = math.sqrt(l)


def term_frequency(term, id):
    if id in postings[term]:
        return postings[term][id]
    else:
        return 0.0


def inverse_document_frequency(term):
    if term in vocabulary:
        return math.log(N / document_frequency[term], 2)
    else:
        return 0.0


def print_scores(scores):
    print("-" * 42)
    print("| %s | %-30s |" % ("Score", "Document"))
    print("-" * 42)

    for (id, score) in scores:
        if score != 0.0:
            print("| %s | %-30s |" % (str(score)[:5], document_filenames[id]))

    print("-" * 42, end="\n\n")


def do_search():
    query = tokenize(input("Search query >> "))

    if query == []:
        sys.exit()

    scores = sorted(
        [(id, similarity(query, id)) for id in range(N)],
        key=lambda x: x[1],
        reverse=True,
    )

    return scores


def intersection(sets):
    return reduce(set.intersection, [s for s in sets])


def similarity(query, id):
    similarity = 0.0

    for term in query:

        if term in vocabulary:
            similarity += term_frequency(term, id) * inverse_document_frequency(term)

    similarity = similarity / length[id]

    return similarity


def remove_special_characters(text):
    regex = re.compile(r"[^a-zA-Z0-9\s]")
    return re.sub(regex, "", text)


def remove_digits(text):
    regex = re.compile(r"\d")
    return re.sub(regex, "", text)



if __name__ == "__main__":
    main()