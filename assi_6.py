def find():
    text = variable1.get()
    suffix = [text[i:] for i in range(len(text))]
    Sortedsuffix = sorted([text[i:] for i in range(len(text))])
    print("Suffixarray:", Sortedsuffix)
    SuffixArray = [suffix.index(ss) for ss in Sortedsuffix]
    print(SuffixArray)
    return [SuffixArray, Sortedsuffix]
def bisect_left(lo=0, hi=None):
    m=find()
    a=m[0]
    text=variable1.get()
    x=variable2.get()
    if lo < 0:
        raise ValueError('lo must be non negative')
    if hi is None:
        hi = len(a)
    #Binary search
    while lo < hi:
        mid = (lo+hi)//2
        if text[a[mid]:] == x:
            return a[mid]
        elif text[a[mid]:] < x:
            lo = mid+1
        else:
            hi = mid
    if not text[a[lo]:].startswith(x):
        raise IndexError('not found')
    listNodes = Listbox(root, width=80,height=15)
    listNodes.grid(column=0, row=12)
    listNodes.insert(END,"\nSuffixArray: {}".format(m[0]))
    listNodes.insert(END, "\nSuffixIndexArray: {}".format(m[1]))
    listNodes.insert(END, "\n\nPatter Found In Suffix Array at Index : {}".format(a[lo]))
    print(a[lo])
from tkinter import *
root = Tk()
root.geometry("500x550")
root.title('Suffix Array and Searching using Suffix Array')
var = IntVar()
variable1=StringVar() # Value saved here
variable2=StringVar() # Value saved here
Label(root, text = "Suffix Array and Searching using Suffix Array: ").grid(row=4, sticky=W)
Label(root, text = "Enter String: ").grid(row=6, sticky=W)
Entry(root, width=30, textvariable=variable1).place(y=25, x=130)
Label(root, text = "Enter Pattern: ").grid(row=8, sticky=W)
Entry(root, width=30, textvariable=variable2).place(y=45, x=130)
Button(root, text = "Show Results", command=bisect_left).grid(row=10, sticky=W)
Label(root, text="Jatan Shah B.Tech IT").place(x=5, y=450)
root.mainloop()