class Column:
    def __init__(self, colNum, boxes):
        boxStart = [0,0,0,1,1,1,2,2,2]
        boxCol = [0,1,2,0,1,2,0,1,2]

        self.colNum = colNum
        self.cells = []

        [[self.cells.append(cell) for cell in box.getCellCol(boxCol[colNum])] for box in boxes[boxStart[colNum]:len(boxes):3]]    
        #print([cell.value for cell in self.cells])

    def check(self):
        valueList = [cell.value for cell in self.cells if cell.value != 0]
        
        if (len(valueList) != len(set(valueList))):
            print( "Check for col " + str(self.colNum) + " " + str(len(valueList) == len(set(valueList))) )
