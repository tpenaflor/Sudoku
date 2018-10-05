from src.Board import Board

path = "sudoku1.csv"
mySudoku = Board()

def updatePossibilities(cell, val):    
    #print(cell.detail())
    boxEmptyCells = [item for item in mySudoku.Boxes[cell.boxNum].cells if item.value == 0]    
    for item in boxEmptyCells:
        #print("box " +str(item.detail()) + str(item.possibles))
        if (len(item.possibles) != 0) and (val in item.possibles):
            item.possibles.remove(val)

    rowEmptyCells = [item for item in mySudoku.Rows[cell.rowNum].cells if item.value == 0]    
    #print("row num " + str(cell.rowNum) + " " + str(cell.detail()))
    for item in rowEmptyCells:
        #print("row " +str(item.detail()) + str(item.possibles))
        if (len(item.possibles) != 0) and (val in item.possibles):
            item.possibles.remove(val)

    colEmptyCells = [item for item in mySudoku.Cols[cell.colNum].cells if item.value == 0]    
    for item in colEmptyCells:
        #print("col " +str(item.detail()) + str(item.possibles))
        if (len(item.possibles) != 0) and (val in item.possibles):
            item.possibles.remove(val)
    
def updateCell(cell, val, solution):
    cell.setVal(val)
    updatePossibilities(cell, val)     
    print("Cell "+ str(cell.detail()) + solution + str(val))
    return True

def solution2(cell): 
    if cell.value != 0 : return
        
    emptyBox = [item for item in mySudoku.Boxes[cell.boxNum].cells if cell != item and item.value == 0]
    emptyRow = [item for item in mySudoku.Rows[cell.rowNum].cells if cell != item and item.value == 0]
    emptyCol = [item for item in mySudoku.Cols[cell.colNum].cells if cell != item and item.value == 0]   

    boxPos = set([val for item in emptyBox for val in item.possibles])
    poss = [item for item in cell.possibles if item not in boxPos]    
    if (len(poss) == 1) : return updateCell(cell, poss[0], " sol2.1 answered ")

    rowPos = set([val for item in emptyRow for val in item.possibles])
    poss = [item for item in cell.possibles if item not in rowPos]   
    if (len(poss) == 1) : return updateCell(cell, poss[0], " sol2.2 answered ")

    colPos = set([val for item in emptyCol for val in item.possibles])
    poss = [item for item in cell.possibles if item not in colPos] 
    if (len(poss) == 1) : return updateCell(cell, poss[0], " sol2.3 answered ")

    return False
    


def solution1(cell):
    if cell.value != 0 : return
    temp = [1,2,3,4,5,6,7,8,9]
    cell.possibles = []

    boxVals = [item.value for item in mySudoku.Boxes[cell.boxNum].cells if item.value != 0]
    rowVals = [item.value for item in mySudoku.Rows[cell.rowNum].cells if item.value != 0]
    colVals = [item.value for item in mySudoku.Cols[cell.colNum].cells if item.value != 0]    
    cell.possibles = [item for item in temp if item not in set(boxVals+rowVals+colVals)]


    # print(cell.detail())
    # print("Box val: " + str(cell.boxNum) + " " + str(boxVals))
    # print("Row val: " + str(cell.rowNum) + " " +  str(rowVals))
    # print("Col val: " + str(cell.colNum) + " " +  str(colVals))
    # print("Pos val: " + str(cell.possibles))
    if (len(cell.possibles) == 1):
        return updateCell(cell, cell.possibles[0], " sol1 answered ")

    return False

def solveIt(tries):    
    cells = mySudoku.getCells()
    emptyCells = [cell for cell in cells if cell.value == 0]

    count = len(emptyCells)
    loopCount = 1
    loopSuccess = True
    while count > 0 and loopCount != tries and loopSuccess:
        print ("Loop# " + str(loopCount))
        loopSuccess = False

        for cell in emptyCells:
           if solution1(cell) : loopSuccess = True

        for cell in emptyCells:                
           if solution2(cell) : loopSuccess = True

        emptyCells = [cell for cell in cells if cell.value == 0]
        loopCount += 1
        count = len(emptyCells)

    print("Logical solving ended at loop: " + str(loopCount))
    print("Remaming empty cells: " + str(len([item for item in emptyCells if item.value == 0])))
    return loopSuccess

def initBrute(cells, pos):
    [item.setVal(0) for item in cells]
    cells[0].possibles = pos

def doBrute(attempt):
    cells = [item for item in mySudoku.getCells() if item.value == 0]
    cells.sort(key = lambda c : len(c.possibles))
    updateCell(cells[0], cells[0].possibles[attempt], " brute forced 1")
    solveIt(0)

    cells = [item for item in mySudoku.getCells() if item.value == 0]
    if len(cells) == 0 : return print("success!!!")
        
    cells.sort(key = lambda c : len(c.possibles))
    isDeadLock = len(cells[0].possibles) != 0
    print("isDeadlock?: " + str(isDeadLock))
    print("end brute 1")
    return {"DeadLock":isDeadLock, "Attempt":attempt}

def bruteForce():
    sureCells = [item for item in mySudoku.getCells() if item.value == 0]
    sureCells.sort(key = lambda c : len(c.possibles))
    baseAssumptions = sureCells[0].possibles

    bruteRes = [sureCells, baseAssumptions]

    for attempt in range(baseAssumptions):
        doBrute(1)

    cells = [item for item in mySudoku.getCells() if item.value == 0]
    cells.sort(key = lambda c : len(c.possibles))
    updateCell(cells[0], cells[0].possibles[attempt], " brute forced 1")
    solveIt(0)

    cells = [item for item in mySudoku.getCells() if item.value == 0]
    if len(cells) == 0 : return print("success!!!")
        
    cells.sort(key = lambda c : len(c.possibles))
    isDeadLock = len(cells[0].possibles) != 0
    print("isDeadlock?: " + str(isDeadLock))
    print("end brute 1")

    # cells = [item for item in mySudoku.getCells() if item.value == 0]
    # cells.sort(key = lambda c : len(c.possibles))
    # updateCell(cells[0], cells[0].possibles[0], " brute forced 2")
    # solveIt(0)
    # cells = [item for item in mySudoku.getCells() if item.value == 0]
    # print([item.possibles for item in cells])
    # print("end brute 2")

    # cells = [item for item in mySudoku.getCells() if item.value == 0]
    # cells.sort(key = lambda c : len(c.possibles))
    # updateCell(cells[0], cells[0].possibles[0], " brute forced 3")
    # solveIt(0)
    # cells = [item for item in mySudoku.getCells() if item.value == 0]
    # print([item.possibles for item in cells])
    # print("end brute 3")
    

    # cells = [item for item in mySudoku.getCells() if item.value == 0]
    # cells.sort(key = lambda c : len(c.possibles))
    # updateCell(cells[0], cells[0].possibles[0], " brute forced 3")
    # solveIt(0)
    # cells = [item for item in mySudoku.getCells() if item.value == 0]
    # print([item.possibles for item in cells])
    # print("end brute 3")

    # for attempt in range(len(cells[0].possibles)):
    #     bruteSuccess = False
    #     while not bruteSuccess:    
    #         updateCell(cells[0], cells[0].possibles[attempt], " brute forced ")
    #         bruteSuccess = solveIt(0)
            
    #         brutes = [item for item in mySudoku.getCells() if item.value == 0]
    #         brutes.sort(key = lambda c : len(c.possibles))
    #         print([item.possibles for item in brutes])

    #         bruteSuccess = True
    #         print("end while")

        
    #     #cells = [item for item in mySudoku.getCells() if item.value == 0]
    #     if len([item for item in mySudoku.getCells() if item.value == 0]) == 0 :
    #         print("success")


        




mySudoku.fillTable(path)

mySudoku.print()

solveIt(0)

print("answered")
mySudoku.print()

print("Brute Forcing -- start")
bruteForce()
print("Brute Forcing -- end")
mySudoku.print()
mySudoku.check()