class Column:
    def __init__(self, colNum, boxes):
        boxStart = [1,1,1,2,2,2,3,3,3]
        boxCol = [1,2,3,1,2,3,1,2,3]

        self.colNum = colNum
        self.cells = []

        [[self.cells.append(cell) for cell in box.getCellCol(boxCol[colNum-1])] for box in boxes[boxStart[colNum-1]-1:len(boxes):3]]    
        #print([cell.value for cell in self.cells])

    def check(self):
        valueList = [cell.val() for cell in self.cells if cell.val() != 0]
        
        if (len(valueList) != len(set(valueList))):
            print( "Check for col " + str(self.colNum) + " " + str(len(valueList) == len(set(valueList))) )
