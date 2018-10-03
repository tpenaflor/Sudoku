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
        self.Boxes = [Box(num+1) for num in range(9)]
        self.Rows = [Row(num+1, self.Boxes) for num in range(9)]
        self.Cols = [Column(num+1, self.Boxes) for num in range(9)]

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
            if (row.rowNum == 4) or (row.rowNum == 7): print(" ")
            row.print()
                            
    def check(self):
        [box.check() for box in self.Boxes]
        [row.check() for row in self.Rows]
        [col.check() for col in self.Cols]

