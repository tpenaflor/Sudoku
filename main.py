from src.Board import Board

path = "sudoku.csv"
mySudoku = Board()

mySudoku.fillTable(path)

mySudoku.print()
mySudoku.check()