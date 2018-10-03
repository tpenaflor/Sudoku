from . import Cell

class Box:
    def __init__(self, boxNum):
        self.boxNum = 0
        self.cells = []

        self.boxNum = boxNum
        for row in range(3):
            for col in range(3):
                self.cells.append(Cell.Cell(row,col,boxNum))

        #print(str(self.boxNum) + " is created with " + str(len(self.cells)) + " cells")
        #self.print()
    
    def getCellRow(self, rowNum):
        start = (rowNum-1) * 3
        return self.cells[start:start + 3]
        
    def getCellCol(self, colNum):
        return self.cells[colNum-1:len(self.cells):3]

    def print(self):
        for start in range (0, len(self.cells), 3):
            cellRow =  self.cells[start:start + 3]
            print("  " + str(cellRow[0].val()) + "  " + str(cellRow[1].val()) + "  " + str(cellRow[2].val()) + "  ")
        
    def check(self):
        valueList = [cell.val() for cell in self.cells if cell.val() != 0]

        if (len(valueList) != len(set(valueList))):
            print( "Check for box " + str(self.boxNum) + " " + str(len(valueList) == len(set(valueList))) )

