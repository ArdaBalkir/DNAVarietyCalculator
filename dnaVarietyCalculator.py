

print("Welcome to The DNA variety calculator")
dna1 = input("Please enter DNA strand one")
dna2 = input("Please enter DNA strand two")

dna1 = dna1.upper()
dna2 = dna2.upper()

def split(word):
    return list(word)


#comparisonfunction
def dnaCompare(d1, d2):
    if len(d1) == len(d2):
        print("The strands are not of matching size")

    d1 = split(d1)
    d2 = split(d2)

    varCnt = 0
    #variety calculation
    for i in range(len(d1)):
        if d1[i] == d2[i]:
            varCnt +=1
    varience = varCnt / len(d1) * 100

    print("Varience percentage is {}%".format(varience))

dnaCompare(dna1,dna2)
