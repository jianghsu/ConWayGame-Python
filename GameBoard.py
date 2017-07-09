import numpy as np
import os

class GameBoard:
   sizeRow = 0
   sizeCol = 0
   board = [[]]

   def __init__(self, r, c):
      GameBoard.sizeRow = r
      GameBoard.sizeCol = c
      GameBoard.board = np.zeros((r, c),dtype=np.int)
       
   def setRandomValue(self):
       #Randomlize the value in the board.
       GameBoard.board = np.matrix(np.random.randint(0,2, size=(GameBoard.sizeRow, GameBoard.sizeCol)))
       return 0

   def setValue(self, r, c, v):
       #Randomlize the value in the board.
       GameBoard.board[r,c] = v
       
   def displayBoard(self):
       #show the game board.
       os.system('clear') 
       for i in range(GameBoard.sizeRow):
           for j in range(GameBoard.sizeCol):
               print GameBoard.board[i,j],
           print "\n"
       return 0
           
   def displayLive(self):
       #show number of live for each cell. 
       print "\n"
       for i in range(GameBoard.sizeRow):
           for j in range(GameBoard.sizeCol):
               print self.numLive(i,j),
           print "\n"
       return 0
 
   def numLive(self, r, c):
       num = 0
       for i in range(r-1,r+2):
           for j in range(c-1,c+2):
               if (i >= 0) & (i < GameBoard.sizeRow) & (j >= 0) & (j < GameBoard.sizeCol):
                   num = num + GameBoard.board[i,j]
       num-=GameBoard.board[r,c]
       return num

   def playGame(self):
       gb = np.zeros((GameBoard.sizeRow, GameBoard.sizeCol),dtype=np.int)
       for i in range(0,GameBoard.sizeRow):
           for j in range(0,GameBoard.sizeCol):
               if ((GameBoard.board[i,j]==1) & (self.numLive(i,j)==2) | (self.numLive(i,j)==3)):
                   gb[i,j]=1
       GameBoard.board = gb
       self.displayBoard()
       return 0
 
def playControl():
    print "Welcome to Conway Game!"  
    r = input("Please input the size of rows:")
    c = input("Please input the size of columes:")
    print "Generating randomlized GameBoard ......"
    gb = GameBoard(r,c)
    gb.setRandomValue()     
    gb.displayBoard()
    next = raw_input("Want to play? (y or n)")
    while (next == "y"):
        gb.playGame()
        next = raw_input("Continue? (y or n)")
    return 0
    
playControl()