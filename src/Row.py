class Row:
    def __init__(self, rowNum, boxes):
        boxStart = [0,0,0,3,3,3,6,6,6]
        boxRow = [1,2,3,1,2,3,1,2,3]

        self.rowNum = rowNum
        self.cells = []

        [[self.cells.append(cell) for cell in box.getCellRow(boxRow[rowNum-1])] for box in boxes[boxStart[rowNum-1]:boxStart[rowNum-1] + 3]]        
        #print([cell.value for cell in self.cells])

    def check(self):
        valueList = [cell.val() for cell in self.cells if cell.val() != 0]
        
        if (len(valueList) != len(set(valueList))):
            print( "Check for row " + str(self.rowNum) + " " + str(len(valueList) == len(set(valueList))) )

    def print(self):
        print("| "+str(self.cells[0].value)+" "+str(self.cells[1].value)+" "+str(self.cells[2].value)\
             +" | "+str(self.cells[3].value)+" "+str(self.cells[4].value)+" "+str(self.cells[5].value)\
             +" | "+str(self.cells[6].value)+" "+str(self.cells[7].value)+" "+str(self.cells[8].value)+" |")

    def fill(self, values):
        for cell, val in zip(self.cells,values):
            try:
                val = int(val)
            except:
                val = 0

            cell.value = val
