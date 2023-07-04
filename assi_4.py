import os
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk

nltk.download('stopwords')
nltk.download('wordnet')


def get_docs(dataset_path):
    docs = []
    for doc_file in os.listdir(dataset_path):
        docs.append(os.path.join(dataset_path, doc_file))
    return docs


dataset_path = "D:\jatan-ir\docs"
print(dataset_path)
docs = get_docs(dataset_path)
print(docs)
corpus = []
stop_words = set(stopwords.words('english'))
for doc in docs:
    with open(doc, mode='r') as f:
        text = f.read()
        word_tokens = word_tokenize(text)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        filtered_sentence = []
        for w in word_tokens:
            if (w not in stop_words) and (w not in ".,/!@#$%^&*()_+={}[]|:0123456789 ;'") and len(w) >= 2:
                filtered_sentence.append(w)
        corpus.append(list(set(filtered_sentence)))
print(corpus)
from tkinter import *

root = Tk()
root.geometry("500x550")
root.title('Pattern Matching')
var = IntVar()
variable1 = StringVar()  # Value saved here
variable2 = StringVar()  # Value saved here
var.set(1)


def quit_loop():
    print("Selection:", var.get())
    global selection
    global query
    query = variable1.get()
    selection = var.get()
    result = []
    listNodes = Listbox(root, width=80, height=7)
    listNodes.grid(column=0, row=12)
    if selection == 1:
        for i in range(len(corpus)):
            for m in corpus[i]:
                if m.startswith(query):
                    print(docs[i])
                    result.append(docs[i])
        result = list(set(result))
        for i in result:
            listNodes.insert(END, i)
    elif selection == 2:
        for i in range(len(corpus)):
            for m in corpus[i]:
                if m.endswith(query):
                    result.append(docs[i])
        result = list(set(result))
        for i in result:
            listNodes.insert(END, i)
    elif selection == 3:
        for i in range(len(corpus)):
            if query in corpus[i]:
                result.append(docs[i])
        result = list(set(result))
        for i in result:
            listNodes.insert(END, i)
    elif selection == 4:
        def show():
            from nltk.metrics import edit_distance
            res = []
            for i in range(len(corpus)):
                for m in corpus[i]:
                    if (int(variable2.get()) > edit_distance(query, m)):
                        res.append(docs[i])
            res = list(set(res))
            for i in res:
                listNodes.insert(END, i)

        Label(root, text="Enter Min, Edit Distance : ").grid(row=9, sticky=W)
        Entry(root, width=30, textvariable=variable2).place(y=160, x=150)
        Button(root, text="Show Results", command=show).place(y=160, x=350)
    else:
        print("Select Proper Button")


Label(root, text="Select Query Processing Methon: ").grid(row=0, sticky=W)
Radiobutton(root, text="Prefix", variable=var, value=1).grid(row=1, sticky=W)
Radiobutton(root, text="Suffix", variable=var, value=2).grid(row=2, sticky=W)
Radiobutton(root, text="Query Match", variable=var, value=3).grid(row=3, sticky=W)
Radiobutton(root, text="Edit Distance", variable=var, value=4).grid(row=4, sticky=W)
Label(root, text="Enter Query").grid(row=6, sticky=W)
Entry(root, width=30, textvariable=variable1).place(y=125, x=90)
Button(root, text="Show Results", command=quit_loop).grid(row=8, sticky=W)
Label(root, text="Jatan Shah B.Tech IT ").place(x=5, y=450)
root.mainloop()