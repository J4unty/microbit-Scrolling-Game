import unittest
import sys, os
from io import StringIO

sys.path.append(os.path.join(os.path.dirname(__file__), "../src/"))

from scrolling_game import *

brightnessPlayer = 9
brightnessBlock = 4
brightnessDefault = 0

class GenerateBoard(unittest.TestCase):
    def test_list_length(self):
        """Test the generate line function"""
        result = generateBoard()
        self.assertEqual(len(result), 5)
        for xCoordinate in range(len(result)):
            self.assertEqual(len(result[xCoordinate]), 5)

    def test_list_contents(self):
        """Tests the content of the generate line function"""
        result = generateBoard()
        for xCoordinate in range(len(result)):
            for yCoordinate in range(len(result[xCoordinate])):
                self.assertEqual(result[xCoordinate][yCoordinate], "")

class CopyBoard(unittest.TestCase):
    def test_copy_basic(self):
        testList = [["1234", "345"], ["12", "345"]]
        result = copyBoard(testList)
        for xCoordinate in range(len(result)):
            for yCoordinate in range(len(result[xCoordinate])):
                self.assertEqual(str(testList[xCoordinate][yCoordinate]), str(result[xCoordinate][yCoordinate]))
        
    def test_copy_advanced(self):
        """Test if copy method works on modify"""
        a = ["12", "23"]
        b = ["abc", "def"]
        testList = [a, b]
        result = copyBoard(testList)
        a[0] = "hello"
        self.assertNotEqual(str(testList[0][0]), str(result[0][0]))

class TranslateValue(unittest.TestCase):
    def test_translateValue_all(self):
        """Test the brigness values"""
        self.assertEqual(translateValue("P"), brightnessPlayer)
        self.assertEqual(translateValue("B"), brightnessBlock)
        self.assertEqual(translateValue(""), brightnessDefault)
    
    def test_random_value(self):
        """Test the default brighness"""
        self.assertEqual(translateValue("abcdef"), brightnessDefault)

class TranslateBoard(unittest.TestCase):
    p = str(brightnessPlayer)
    b = str(brightnessBlock)
    d = str(brightnessDefault)

    def test_translateBoard_2x2(self):
        testBoard = [["P", "B"],["", "X"]]
        result = translateBoard(testBoard)
        expected = self.p + self.b + ":" + self.d + self.d
        self.assertEqual(result, expected)

    def test_translateBoard_4x1(self):
        testBoard = [["c"], ["B"], [""], ["P"]]
        expected = self.d + ":" + self.b + ":" + self.d + ":" + self.p
        result = translateBoard(testBoard)
        self.assertEqual(result, expected)

class PrintBoard(unittest.TestCase):
    def test_printBoard(self):
        """we cannot test this due to the nececety to mock stubs, we can only test the signature"""
        printBoard([["c"], ["B"], [""], ["P"]])

class MovePlayer(unittest.TestCase):
    def test_movePlayer_basic(self):
        board = generateBoard()
        
        movePlayer(board, -1)
        result = drawPlayer(copyBoard(board))
        self.assertEqual(translateValue(result[4][1]), brightnessPlayer)

        movePlayer(board, 2)
        result = drawPlayer(copyBoard(board))
        self.assertEqual(translateValue(result[4][3]), brightnessPlayer)

    def test_movePlayer_fallOver(self):
        board = generateBoard()
        
        movePlayer(board, 3)
        result = drawPlayer(copyBoard(board))
        self.assertEqual(translateValue(result[4][1]), brightnessPlayer)

        movePlayer(board, -2)
        result = drawPlayer(copyBoard(board))
        self.assertEqual(translateValue(result[4][4]), brightnessPlayer)

class GenerateLine(unittest.TestCase):
    def test_generateLine_basic(self):
        result = generateLine()
        self.assertIn("B", result)
        self.assertEqual(len(result), 5)
        self.assertGreaterEqual(result.count("B"), 1)

class MoveDown(unittest.TestCase):
    def test_moveDown_basic(self):
        board = [
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", "B"],
            ["", "", "P", "", ""]
            ]
        moveDown(board)
        self.assertNotEqual(board[4][2], "P")
        self.assertEqual(board[4][4], "B")
        self.assertEqual(len(board), 5)
        self.assertGreaterEqual(board[0].count("B"), 1)

if __name__ == '__main__':
    unittest.main()
