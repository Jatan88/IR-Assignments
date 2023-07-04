import tkinter as t
from tkinter import *
from tkinter import ttk
import tkinter.font as font


def KMP():
    txt = txt1.get()
    pat = pat1.get()
    M = len(pat)
    N = len(txt)
    lps = [0] * M
    j = 0
    LPS_Arr(pat, M, lps)
    i = 0
    c = 55

    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            ttk.Label(window, text="\n Pattern Found at index : " + str(i - j)).grid(row=c, column=0, padx=10, pady=10)
            c += 10
            j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def LPS_Arr(pat, M, lps):
    len = 0
    lps[0]
    i = 1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


window = t.Tk(className='Roll No.: 36')
window.title("KMP algorithm")
window.geometry('500x400')

newFont = font.Font(size=20)

ttk.Label(window, text=' KMP Algorithm ', foreground='black', background='skyblue',
          font=('Times New Romen', 15)).grid(row=0, column=1, pady=10, padx=5)
txt1 = t.StringVar()
pat1 = t.StringVar()
text_label = t.Label(window, text=' Enter Text :', font=('calibre', 10)).grid(row=35, column=0, padx=5, pady=5)
text_entry = t.Entry(window, width=30, textvariable=txt1, font=('calibre', 10, 'normal')).grid(row=35, column=1, padx=5,
                                                                                               pady=5)
pat_label = t.Label(window, text=' Enter Pattern :', font=('calibre', 10)).grid(row=45, column=0, padx=5, pady=5)
pat_entry = t.Entry(window, width=30, textvariable=pat1, font=('calibre', 10, 'normal')).grid(row=45, column=1, padx=5,
                                                                                              pady=5)
sub_btn = Button(window, font=('calibre', 10, 'normal'), text='Search ', command=KMP).grid(row=47, column=1, padx=5,
                                                                                           pady=5)
window.configure(bg='lightblue')
window.mainloop()
