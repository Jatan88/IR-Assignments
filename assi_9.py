from tkinter import *
import tkinter as tk
from tkinter import messagebox


# Top level window

frame = tk.Tk()
frame.title("Boyre Moore")
frame.geometry('500x300')

#  label
lbl = Label(frame, text="Text :", bg = "light blue",font="Times ")
lbl.grid(column=0, row=1)
lbl.configure(foreground="black")
#  field
txt_field = Entry(frame, width=30)
txt_field.grid(column=1, row=1)

#  label
lbl1 = Label(frame, text="Pattern :", bg = "light blue",font="Times")
lbl1.grid(column=0, row=2)
lbl1.configure(foreground="black")
#  field
txt_pattern = Entry(frame, width=30)
txt_pattern.grid(column=1, row=2)

res_list=[]
def Match():

    NO_OF_CHARS = 256

    def badCharHeuristic(string, size):

        # Initialize all occurrence as -1
        badChar = [-1] * NO_OF_CHARS

        # Fill the actual value of last occurrence
        for i in range(size):
            badChar[ord(string[i])] = i;

        # retun initialized list
        return badChar

    def search(txt, pat):
        res_list = []
        if (txt == "" or pat==""):
            messagebox.showinfo("Empty fields","Fill out the fields")

        m = len(pat)
        n = len(txt)

        badChar = badCharHeuristic(pat, m)

        # s is shift of the pattern with respect to text
        s = 0
        while (s <= n - m):
            j = m - 1

            while j >= 0 and pat[j] == txt[s + j]:
                j -= 1

            if j < 0:
                print("Pattern occur at shift = {}".format(s))

                res_list.append(s)

                s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
            else:

                s += max(1, j - badChar[ord(txt[s + j])])

        if res_list==[]:
            lbl4 = Label(frame , text="                    " , font="Times")
            lbl4.grid(column=1 , row=4)
            lbl4.configure(foreground="black")
            messagebox.showinfo("Match Status" , "No Match found")

        else:
            lbl4 = Label(frame , text=",".join(map(str , res_list)) , font="Times")
            lbl4.grid(column=1 , row=4)
            lbl4.configure(foreground="black")

    txt = txt_field.get()
    pat = txt_pattern.get()
    search(txt, pat)    #ouput


b = Button(frame, text="Match", bg = "light blue",command=Match)
b.grid(column=1, row=3)

lbl2 = Label(frame, text="Pattern occur at shifts : ", bg = "light blue",font="Times")
lbl2.grid(column=0, row=4)
lbl2.configure(foreground="black")
frame.configure(bg="skyblue")
frame.mainloop()