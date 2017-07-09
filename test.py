import unittest
from GameBoard import *
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
   
    def test_initGameBoard(self):
        #initialize GameBaord
        gb = GameBoard(1,1)
        self.assertEqual(gb.board[0,0], 0)

    def test_setRandomValue(self):
        print "set Random Value for GameBaord"
        gb = GameBoard(3,4)       
        self.assertEqual(gb.setRandomValue(),0)
        self.assertEqual(gb.displayBoard(),0)

    def test_numLive(self):
        #calculate the number of lives from the neibor
        gb = GameBoard(1,1)
        self.assertEqual(gb.numLive(0,0), 0)

    def test_setValue(self):
        gb = GameBoard(3,4)
        gb.setValue(1,2,1)
        self.assertEqual(gb.board[1,2], 1)
        self.assertEqual(gb.board[1,1], 0)
        
    def test_playGame(self):
        print "play game"
        gb = GameBoard(3,4)
        gb.setRandomValue()     
        self.assertEqual(gb.displayBoard(),0)
        self.assertEqual(gb.displayLive(),0)
        self.assertEqual(gb.playGame(),0)

    def test_playControl(self):
        self.assertEqual(playControl(),0)
 
if __name__ == '__main__':
    unittest.main()
    #playControl()