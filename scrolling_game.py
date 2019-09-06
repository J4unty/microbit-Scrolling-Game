# needed for minimizer
from microbit import display, Image, button_a, button_b, sleep
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
    """Generate a new blank board
    
    Returns:
        (list(list(str))): A new blank board
    """
    ret = []
    for i in range(5):
        ret.append(["","","","",""])
    return ret

def copyBoard(board):
    """Makes a deep copy of a 2D list

    Args:
        board (list(list(str))): The given 2D list
    
    Returns:
        A copy of the given 2D list
    """
    ret = []
    for i in range(len(board)):
        ret.append(board[i].copy())
    return ret

def translateValue(value: str) -> int:
    """Translates the string representation of an Item to an LED brightness

    Args:
        value (str): The given String block
    
    Returns:
        int: The LED brightness value for that block [0,9]
    """
    if value == "P":
        return 9
    elif value == "B":
        return 4
    else:
        return 0

def translateBoard(board):
    """Translates a given board to a 2D LED brightness list

    Args:
        board (list(list(str))): The given board
    
    Returns:
        list(list(int)): The LED brightness 2D list to the given board
    """
    ret = ""
    for i in range(len(board)):
        for j in range(len(board[i])):
            ret += str(translateValue(board[i][j]))
        if i != len(board) - 1:
            ret += ":"
    return ret

def printBoard(board: list(list(int))):
    """Prints the given LED brightness 2D list

    Args:
        board (list(list(str))): The given LED brightness 2D list
    """
    if not gameOverVar:
        display.show(Image(translateBoard(board)))

def drawPlayer(board):
    """Draws the player onto the given 2D string list

    Args:
        board (list(list(str))): The given board
    """
    board[4][playerPosition] = "P"
    return board

def movePlayer(board, step: int):
    """Moves the player left or right.

    Args:
        baord (list(list(str)): the given 2D board
        step (int): The given step, left negative, right positive
    """
    global playerPosition
    playerPosition = (playerPosition + 5 + step) % 5
    checkPlayerPosition(board)

def movement(board):
    """Checks if the player pressed a button and moves him accordingly

    Args:
        board (list(list(str))): The current board
    """
    if button_a.is_pressed():
        movePlayer(board, -1)
    if button_b.is_pressed():
        movePlayer(board, 1)

def checkPlayerPosition(board):
    """Checks if the plyaer is on a block, if yes it displays a Game Over screen

    Args:
        board (list(list(str))): the given board
    """
    if board[4][playerPosition] != "":
        gameOver()

def waitForStart():
    """Waits until the player wants to start a game"""
    display.scroll("Start?")
    display.show(Image.ARROW_W)
    while True:
        if button_a.is_pressed():
            display.clear()
            sleep(150)
            return
        sleep(100)

def gameOver():
    """Displays the Game Over screen, current points and current high score"""
    global gameOverVar, maxScore
    gameOverVar = True
    if playerScore > maxScore:
        maxScore = playerScore
    display.show("GAME OVER")
    display.scroll("Your score: " + str(playerScore) + ", Record: " + str(maxScore), delay=90)

def generateLine() -> list(str):
    """Generates a new Line with a random block

    Returns:
        list(str): A new line for the game, with a random new block
    """
    tmp = ["","","","",""]
    randNum = random.randint(0, 4)
    tmp[randNum] = "B"
    return tmp

def moveDown(board):
    """Moves the given board a line down, and generates a new line on top

    Args:
        board (list(list(str))): The given board
    """
    board.insert(0, generateLine())
    del board[5]
    checkPlayerPosition(board)

def checkLevel():
    """Increseas the playerLevel if needed"""
    if playerScore % 10 == 0:
        increaseLevel()

def increaseLevel():
    """Increases the players level"""
    global playerLevel
    if playerLevel < maxLevel:
        playerLevel += 1

def main():
    global gameOverVar, playerPosition, playerScore, playerLevel
    while True:
        gameOverVar = False
        playerPosition = 2
        playerScore = 0
        playerLevel = 0
        board = generateBoard()
        waitForStart()
        while not gameOverVar:
            # TODO: fix loop bug when crash on i = 0, is it fixed?
            for i in range(10 - playerLevel):
                movement(board)
                printBoard(drawPlayer(copyBoard(board)))
                if gameOver is True:
                    break
                sleep(100)
            checkLevel()
            moveDown(board)
            playerScore += 1

if __name__ == "__main__":
    main()
