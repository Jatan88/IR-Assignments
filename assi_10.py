from tkinter import *
root = Tk()
root.geometry("500x550")
root.title('Shift-OR Sequential Search')


def to_bin(n, width=32):
    "Pad a binary number to WIDTH bits wide"
    s = bin(n).replace("0b", "")
    return (("%0" + str(width) + "d") %  int(s))
def neg(x):
    #0b11111111111111111111111111111111  - x
    return 0b11111111111111111111111111111111  - x
def shift_or():
    trace = True
    text=variable1.get()
    pattern= variable2.get()
    """Same as shift_and, but invert masks  and use OR to 
    avoid an | in the inner loop."""
    m = len(pattern)
    n = len(text)
    neg0 = neg(0)
    # build table
    B = {} #  char -> bitmask table
    for i in range(m):
        B[pattern[i]] = (B.get(pattern[i], 0)  | (1 << i))
    B = {k: neg(B[k]) for k in B}
        # complement all bit masks in B,  complement bit mask
    a = neg0
    hit = (1 << (m - 1))
    listNodes = Listbox(root, width=80,  height=35)
    listNodes.grid(column=0, row=12)
    notf=0
    for i in range(n):
        a = (((a << 1) & neg0) | B.get(text[i], neg0))
        if trace:
            listNodes.insert(END, " %s &  B[%c] : %s" % (to_bin(a), text[i],  to_bin(B.get(text[i], neg0))))
            #print("%s & B[%c] : %s" %  (to_bin(a), text[i], to_bin(B.get(text[i],  neg0))))


        if a & hit == 0:
            listNodes.insert(END,"\nPattern Found at  %d" % (i - m + 2))
            notf=1


    if notf == 0 :
        listNodes.insert(END, "\n Pattern Not Found ")


var = IntVar()
variable1=StringVar()
variable2=StringVar()# Value saved here variable2=StringVar() # Value saved here
Label(root, text = "Shift-OR Sequential  Search: ",background='skyblue' ,foreground='black').grid(row=4, column=3)
Label(root, text = "Enter Text:").grid(row=7, column=2)
Entry(root, width=30,textvariable = variable1).grid(row=7, column=3)
Label(root, text = "Enter Pattern:  ").grid(row=9, column=2)
Entry(root, width=30,textvariable = variable2).grid(row=9, column=3)
Button(root, text = "Show Results",  command= shift_or).grid(row=11, column=3)
root.config(bg="skyblue")
root.mainloop()

#place(y=25, x=130)