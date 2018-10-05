from .Box import Box
from .Row import Row
from .Column import Column
import string
import csv

class Board:
    Boxes = []
    Rows = []
    Cols = []
    cells = []

    def __init__(self):
        self.Boxes = [Box(num) for num in range(9)]
        self.Rows = [Row(num, self.Boxes) for num in range(9)]
        self.Cols = [Column(num, self.Boxes) for num in range(9)]

    def fillTable(self, filePath):
        with open(filePath) as csvfile:
            reader = csv.reader(csvfile)
            for values in reader:
                self.Rows[reader.line_num-1].fill(values)
                if (reader.line_num == 9): break
                
    def print(self):
        # for rowNum in range(9):
        #      print([cell.value for cell in self.Rows[rowNum].cells])
        
        for row in self.Rows:
            if (row.rowNum == 3) or (row.rowNum == 6): print(" ")
            #row.detailedPrint()
            row.print()
                            
    def check(self):
        [box.check() for box in self.Boxes]
        [row.check() for row in self.Rows]
        [col.check() for col in self.Cols]

    def getCells(self):
        cells = []
        for row in self.Rows:
            for cell in row.cells:
                cells.append(cell)

        return cells





