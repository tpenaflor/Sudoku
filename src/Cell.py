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