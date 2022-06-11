from tkinter import * 



root = Tk()
root.title("DNA Strand Varience Calculator")
#root.iconbitmap("dnaico.ico")
root.geometry("320x220")

paddings = {'padx': 15, 'pady': 15}

def split(word):
    return list(word)

dnaList = ["DNASAMPLETCAG"]


e = Entry(root, width=32)
e.grid(column=0,row=0, sticky=W, **paddings)

dna1 = StringVar()


dna2 = StringVar()


dnaDrop1 = OptionMenu(root, dna1, *dnaList)
dnaDrop1.grid(column=0, row=1, sticky=W, **paddings)
dnaDrop2 = OptionMenu(root, dna2, *dnaList)
dnaDrop2.grid(column=0, row=2, sticky=W, **paddings)

def addCl():
    dnaList.append(e.get())
    dnaDrop1 = OptionMenu(root, dna1, *dnaList)
    dnaDrop1.grid(column=0, row=1, sticky=W, **paddings)
    dnaDrop2 = OptionMenu(root, dna2, *dnaList)
    dnaDrop2.grid(column=0, row=2, sticky=W, **paddings)

def cmpCl():
    d1 = dna1.get()
    d2 = dna2.get()

    if len(d1) != len(d2):
        eqlbl = Label(root, text="The strands are not of matching size").grid(column=0,row=3)
        return 

    d1 = split(d1)
    d2 = split(d2)

    varCnt = 0
    #variety calculation
    for i in range(len(d1)):
        if d1[i] == d2[i]:
            varCnt +=1
    varience = varCnt / len(d1) * 100

    vrnStr = "Varience percentage is {}%".format(varience)

    eqlbl = Label(root, text=vrnStr).grid(column=0,row=3)

addButton = Button(root, text="Add", command=addCl)
addButton.grid(column=1,row=1, sticky=W, **paddings) 
cmpButton = Button(root, text="Compare", command=cmpCl)
cmpButton.grid(column=1,row=2, sticky=W, **paddings) 



root.mainloop()