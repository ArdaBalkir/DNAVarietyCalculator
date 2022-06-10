from tkinter import * 



root = Tk()
root.title("DNA Strand Varience Calculator")
#root.iconbitmap("dnaico.ico")
root.geometry("600x600")

def split(word):
    return list(word)

dnaList = ["DNASAMPLETCAG"]


e = Entry(root, width=64)
e.grid(column=0,row=0)

dna1 = StringVar()
dna1.set(dnaList[0])

dna2 = StringVar()
dna2.set(dnaList[0])

dnaDrop1 = OptionMenu(root, dna1, *dnaList)
dnaDrop1.grid(column=0, row=1)
dnaDrop2 = OptionMenu(root, dna2, *dnaList)
dnaDrop2.grid(column=0, row=2)

def addCl():
    dnaList.append(e.get())
    dnaDrop1 = OptionMenu(root, dna1, *dnaList)
    dnaDrop1.grid(column=0, row=1)
    dnaDrop2 = OptionMenu(root, dna2, *dnaList)
    dnaDrop2.grid(column=0, row=2)

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
addButton.grid(column=1,row=1) 
cmpButton = Button(root, text="Compare", command=cmpCl)
cmpButton.grid(column=1,row=2) 



root.mainloop()