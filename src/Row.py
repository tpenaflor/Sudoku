class Row:
    def __init__(self, rowNum, boxes):
        boxStart = [0,0,0,3,3,3,6,6,6]
        boxRow = [0,1,2,0,1,2,0,1,2]

        self.rowNum = rowNum
        self.cells = []

        [[self.cells.append(cell) for cell in box.getCellRow(boxRow[rowNum])] for box in boxes[boxStart[rowNum]:boxStart[rowNum] + 3]]        
        #print([cell.value for cell in self.cells])

    def check(self):
        valueList = [cell.value for cell in self.cells if cell.value != 0]
        
        if (len(valueList) != len(set(valueList))):
            print( "Check for row " + str(self.rowNum) + " " + str(len(valueList) == len(set(valueList))) )

    def print(self):
        print("| "+str(self.cells[0].value)+" "+str(self.cells[1].value)+" "+str(self.cells[2].value)\
             +" | "+str(self.cells[3].value)+" "+str(self.cells[4].value)+" "+str(self.cells[5].value)\
             +" | "+str(self.cells[6].value)+" "+str(self.cells[7].value)+" "+str(self.cells[8].value)+" |")

    def detailedPrint(self):
        print("| "+str(self.cells[0].detail())+" "+str(self.cells[1].detail())+" "+str(self.cells[2].detail())\
             +" | "+str(self.cells[3].detail())+" "+str(self.cells[4].detail())+" "+str(self.cells[5].detail())\
             +" | "+str(self.cells[6].detail())+" "+str(self.cells[7].detail())+" "+str(self.cells[8].detail())+" |")

    def fill(self, values):
        for cell, val in zip(self.cells,values):
            try:
                val = int(val)
            except:
                val = 0

            cell.setVal(val)
