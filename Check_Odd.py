def printOdd(x, y, z):
    oddx = 0
    oddy = 0
    oddz = 0
    isOdd = False
    if x%2 != 0:
        oddx = x
        isOdd = True
    if y%2 != 0:
        oddy = y
        isOdd = True
    if z%2 != 0:
        oddz = z
        isOdd = True
    if isOdd == False:
        print(min(x, y, z))
        return
    print(max(oddx, oddy, oddz))
    
printOdd(2, 4, 6)
printOdd(3, 5, 7)
printOdd(6, 7, 8)
