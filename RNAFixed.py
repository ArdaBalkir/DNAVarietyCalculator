from tkinter import * 
from more_itertools import chunked
#1
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = Tk()
root.title("RNA Strand Varience Calculator")
#root.iconbitmap("dnaico.ico")
root.geometry("400x520")

paddings = {'padx': 15, 'pady': 15}
#creating rna sample database as a list
dnaList = ["DNASAMPLETCAG"]
#setting entry
e = Entry(root, width=32)
e.grid(column=0,row=0, sticky=W, **paddings)

dna1 = StringVar()
dna2 = StringVar()

#creating the dropdown menus for comparison
dnaDrop1 = OptionMenu(root, dna1, *dnaList)
dnaDrop1.grid(column=0, row=1, sticky=W, **paddings)
dnaDrop2 = OptionMenu(root, dna2, *dnaList)
dnaDrop2.grid(column=0, row=2, sticky=W, **paddings)

def addCl():
    """Function to take the entry and add it as a rna strand"""
    dnaList.append(e.get())
    dnaDrop1 = OptionMenu(root, dna1, *dnaList)
    dnaDrop1.grid(column=0, row=1, sticky=W, **paddings)
    dnaDrop2 = OptionMenu(root, dna2, *dnaList)
    dnaDrop2.grid(column=0, row=2, sticky=W, **paddings)

def groupByLetter(str1):
    store = {}
    
    for i in range(len(str1)):
        store[str1[i]] = 1 + store.get(str1[i], 0)
        
    return store
            

def cmpButton():
    cmpCl()
    plotFigures()

def plotFigures():

    fig = Figure(figsize = (4, 3),
                 dpi = 100)

    rnalist = groupByLetter(dna1.get())
    names = list(rnalist.keys())
    values = list(rnalist.values())
 

    plot1 = fig.add_subplot(111)
    
    plot1.bar(range(len(rnalist)), values, tick_label=names) 

    # plotting the graph
    plot1.plot()

    canvas = FigureCanvasTkAgg(fig,
                             master = root)  
    canvas.draw()
    canvas.get_tk_widget().grid(column=0,row=4,columnspan=5,rowspan=15, sticky=W, **paddings) 


def cmpCl():
    d1 = dna1.get()
    d2 = dna2.get()

    if len(d1) != len(d2):
        eqlbl = Label(root, text="The strands are not of matching size").grid(column=0,row=3)
        return 
    #Grouping the strings into mini lists of four to simulate the structure of the rna better
    d1 = list(chunked((list(d1)), 4))
    d2 = list(chunked((list(d2)), 4))

    varCnt = 0
    #variety calculation
    for i in range(len(d1)):
        if d1[i] == d2[i]:
            varCnt +=1
    varience = varCnt / len(d1) * 100

    vrnStr = f"Common gene percentage is {varience}%"
    eqlbl = Label(root, text=vrnStr).grid(column=0,row=3)



    #add and compare buttons here!
addButton = Button(root, text="Add", command=addCl)
addButton.grid(column=1,row=1, sticky=W, **paddings) 
cmpButton = Button(root, text="Compare", command=cmpButton)
cmpButton.grid(column=1,row=2, sticky=W, **paddings) 

root.mainloop()


