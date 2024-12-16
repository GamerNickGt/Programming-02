space = 10
rows = 10
spacebetween = 20
def addspace(i):
    space = ""
    for s in range(i):
        space += " "
    return space
def printchar(c, i):
    pc = c
    for chars in range(i):
        pc += c
    return pc

for i in range(rows):
    #leftside up
    print(printchar("x",i),addspace(spacebetween-rows-i),printchar("o",rows-i))

for j in range(rows+1):
    #leftsde down
    chars = rows-j
    print(printchar("x",chars),addspace(spacebetween-chars-rows),printchar("o",j))
        

