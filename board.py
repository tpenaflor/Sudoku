class Cell:
    def __init__(self,x,y,box):
        self.posX = x
        self.posY = y 
        self.boxNum = box
        #self.value = str(box)+"("+str(x)+","+str(y)+")"
        self.value = 0

    def setVal(self,val):
        self.value = val

    def row(self):
        return self.posX

    def col(self):
        return self.posY

    def val(self):
        return self.value

    def box(self):
        return self.boxNum

class Box:

    def __init__(self, boxNum):
        self.boxNum = 0
        self.cells = []

        self.boxNum = boxNum
        for row in range(3):
            for col in range(3):
                self.cells.append(Cell(row,col,boxNum))

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

    def addCells(self, values):
        start = (rowNum-1) * 3
        for cell, value in self.cells[start:start+3], values :
            cell.value = value



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

import string
import csv

class Sudoku:
    Boxes = []
    Rows = []
    Cols = []

    cells = []

    # def __init__(self):
    #     self.Boxes = [Box(num+1) for num in range(9)]
    #     self.Rows = [Row(num+1, self.Boxes) for num in range(9)]
    #     self.Cols = [Column(num+1, self.Boxes) for num in range(9)]
    def boxFiller(self, rows, boxStart):
        boxVal = []
        for row in rows:
            for val in row[0:len(row):3]:
                boxVal.append(val)
        
        print(boxVal)

        


    def __init__(self, filePath):
        with open(filePath) as csvfile:
            reader = csv.reader(csvfile)
            #print(reader[0])
            # [print(row) for row in reader[0:3]]
            # [print(row) for row in reader[3:6]]
            # [print(row) for row in reader[6:9]]

            # for row in range(9):
            #     reader[row]
            boxStart = 1
            rows = []
            for row in reader:
                rows.append(row)
                if (reader.line_num % 3 == 0) :
                    self.boxFiller(rows, boxStart)
                    boxStart = reader.line_num + 1
                    rows = []


    def print(self):
        # for rowNum in range(9):
        #      print([cell.value for cell in self.Rows[rowNum].cells])
        
        for row in self.Rows:
            if (row.rowNum == 4) or (row.rowNum == 7): print(" ")
            row.print()
                            

    def check(self):
        [box.check() for box in self.Boxes]
        [row.check() for row in self.Rows]
        [col.check() for col in self.Cols]

path = "sudoku.csv"
mySudoku = Sudoku(path)

# mySudoku.print()
# mySudoku.check()