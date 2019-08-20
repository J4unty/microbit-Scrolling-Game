from microbit import *
import random

# notes functions needed:
# better difficulty function

playerPosition = 2
playerScore = 0
playerLevel = 0
maxLevel = 6
maxScore = 0
gameOverVar = False

def generateBoard():
    ret = []
    for i in range(5):
        ret.append(["","","","",""])
    return ret

def copyBoard(board):
    ret = []
    for i in range(len(board)):
        ret.append(board[i].copy())
    return ret

def translateValue(value):
    if value == "P":
        return 9
    elif value == "B":
        return 4
    else:
        return 0

def translateBoard(board):
    ret = ""
    for i in range(len(board)):
        for j in range(len(board[i])):
            ret += str(translateValue(board[i][j]))
        if i != len(board) - 1:
            ret += ":"
    return ret

def printBoard(board):
    if not gameOverVar:
        display.show(Image(translateBoard(board)))

def drawPlayer(board):
    board[4][playerPosition] = "P"
    return board

# step, left negative, right positive
def movePlayer(board, step):
    global playerPosition
    playerPosition = (playerPosition + 5 + step) % 5
    checkPlayerPosition(board)

def movement(board):
    if button_a.is_pressed():
        movePlayer(board, -1)
    if button_b.is_pressed():
        movePlayer(board, 1)

def checkPlayerPosition(board):
    if board[4][playerPosition] != "":
        gameOver()

def waitForStart():
    display.scroll("Start?")
    display.show(Image.ARROW_W)
    while True:
        if button_a.is_pressed():
            display.clear()
            sleep(150)
            return
        sleep(100)

def gameOver():
    global gameOverVar, maxScore
    gameOverVar = True
    if playerScore > maxScore:
        maxScore = playerScore
    display.show("GAME OVER")
    display.scroll("Your score: " + str(playerScore) + ", Record: " + str(maxScore), delay=90)

def generateLine():
    tmp = ["","","","",""]
    randNum = random.randint(0, 4)
    tmp[randNum] = "B"
    return tmp

def moveDown(board):
    board.insert(0, generateLine())
    del board[5]
    checkPlayerPosition(board)

def checkLevel():
    if playerScore % 10 == 0:
        increaseLevel()

def increaseLevel():
    global playerLevel
    if playerLevel < maxLevel:
        playerLevel += 1

while True:
    gameOverVar = False
    playerPosition = 2
    playerScore = 0
    playerLevel = 0
    board = generateBoard()
    waitForStart()
    while not gameOverVar:
        for i in range(10 - playerLevel):
            movement(board)
            printBoard(drawPlayer(copyBoard(board)))
            sleep(100)
        checkLevel()
        moveDown(board)
        playerScore += 1
