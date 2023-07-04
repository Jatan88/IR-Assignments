from tkinter import *
def Ass(string, sub_str):
    for i in range(len(string) - len(sub_str) + 1):
        index = i
        for j in range(len(sub_str)):
            if string[index] == sub_str[j]:
                index += 1
            else:
                break
            if index - i == len(sub_str):
                return "Pattern found at index : "+str(i)
    return "Pattern Not Found"
def mhello():
    mtext = ment.get()
    pat1 = pat.get()
    output = Ass(mtext, pat1)
    mlabel1 = Label(mgui, text=output).pack()
    return
mgui = Tk()
ment = StringVar()
pat = StringVar()
mgui.geometry('450x450+500+300')
mgui.title('Brute Force')
mlabel = Label(mgui, text=' Brute force Algorithm :').pack()
mlabel2 = Label(mgui,bg="skyblue" ,text="ENTER THE TEXT").pack()
mentry = Entry(mgui, textvariable=ment).pack()
mlabel2 = Label(mgui, bg="skyblue",text="ENTER THE PATTERN").pack()
mentry1 = Entry(mgui, textvariable=pat).pack()
mbutton = Button(mgui, text="Find the pattern", command=mhello, fg='black', bg='skyblue').pack()
mgui.configure(bg="skyblue")
mgui.mainloop()
