from . import Cell

class Box:
    def __init__(self, boxNum):
        self.boxNum = boxNum
        self.cells = []

        self.boxNum = boxNum
        for row in range(3):
            for col in range(3):
                self.cells.append(Cell.Cell(col,row,boxNum))

        #print(str(self.boxNum) + " is created with " + str(len(self.cells)) + " cells")
        #self.print()
    
    def getCellRow(self, rowNum):
        start = (rowNum) * 3
        return self.cells[start:start + 3]
        
    def getCellCol(self, colNum):
        return self.cells[colNum:len(self.cells):3]

    def print(self):
        for start in range (0, len(self.cells), 3):
            cellRow =  self.cells[start:start + 3]
            print("  " + str(cellRow[0].value) + "  " + str(cellRow[1].value) + "  " + str(cellRow[2].value) + "  ")
        
    def check(self):
        valueList = [cell.value for cell in self.cells if cell.value != 0]

        if (len(valueList) != len(set(valueList))):
            print( "Check for box " + str(self.boxNum) + " " + str(len(valueList) == len(set(valueList))) )

    def updateCells(self):
        currentVal = [cell.value for cell in self.cells if cell.value != 0]
        emptyCells = [cell for cell in self.cells if cell.value == 0]

        for cell in emptyCells:
            temp = [item for item in cell.possibles if not item in currentVal]
            cell.possibles = temp

