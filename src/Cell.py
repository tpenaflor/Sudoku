import math
class Cell:
    def __init__(self,x,y,box):
        self.posX = x
        self.posY = y 
        self.boxNum = box
        #self.value = str(box)+"("+str(x)+","+str(y)+")"
        self.value = 0

        matrix = [[0,1,2],[3,4,5],[6,7,8]]

        boxCol = [0,1,2,0,1,2,0,1,2]
        self.colNum = matrix[boxCol[self.boxNum]][self.posX]
        
        boxRow = [0,0,0,1,1,1,2,2,2]
        self.rowNum = matrix[boxRow[self.boxNum]][self.posY]

        self.possibles = []

    def setVal(self,val):
        self.value = val

    def row(self):
        return self.posX

    def col(self):
        return self.posY

    def box(self):
        return self.boxNum
        
    def detail(self):
        #return ("("+str(self.boxNum) + "," + str(self.rowNum) + "," + str(self.colNum)+", '"+ str(self.value) +"' )")
        return str(self.boxNum) +" ("+ str(self.colNum) + "," + str(self.rowNum) + ") Val: " + str(self.value) + " " + str(self.possibles)


