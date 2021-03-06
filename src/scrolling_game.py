# needed for minimizer
from microbit import display, Image, button_a, button_b, sleep

# needed for the uinittests
from typing import List # Remove this line before manual micro:bit upload

import random

# notes functions needed:
# better difficulty function

playerPosition = 2
playerScore = 0
playerLevel = 0
maxLevel = 6
maxScore = 0
gameOverVar = False

def generateBoard() -> List[List[str]]:
    """Generate a new blank board

    Returns:
        (List[List[str]]): A new blank board
    """
    ret = []
    for index in range(5):
        ret.append(["", "", "", "", ""])
    return ret

def copyBoard(board: List[List[str]]) -> List[List[str]]:
    """Makes a deep copy of a 2D list

    Args:
        board (list(list(str))): The given 2D list

    Returns:
        List[List[str]]: A copy of the given 2D list
    """
    ret = []
    for index in range(len(board)):
        ret.append(board[index].copy())
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

def translateBoard(board: List[List[str]]) -> str:
    """Translates a given board to a 2D LED brightness list

    Args:
        board (List[List[str]]): The given board

    Returns:
        str: The LED brightness string to the given board
    """
    # TODO: replace this with an awesome reduce oneliner
    ret = ""
    for yCoordinate in range(len(board)):
        for xCoordinate in range(len(board[yCoordinate])):
            ret += str(translateValue(board[yCoordinate][xCoordinate]))
        if yCoordinate != len(board) - 1:
            ret += ":"
    return ret

def printBoard(board: List[List[str]]) -> None:
    """Prints the given LED brightness 2D list

    Args:
        board (List[List[str]]): The given LED brightness 2D list
    """
    if not gameOverVar:
        display.show(Image(translateBoard(board)))

def drawPlayer(board: List[List[str]]) -> List[List[str]]:
    """Draws the player onto the given 2D string list

    Args:
        board (List[List[str]]): The given board

    Returns:
        List[List[str]]: the modfied board given as parameter
    """
    board[4][playerPosition] = "P"
    return board

def movePlayer(board: List[List[str]], step: int) -> None:
    """Moves the player left or right.

    Args:
        baord (List[List[str]]): the given 2D board
        step (int): The given step, left negative, right positive
    """
    global playerPosition
    playerPosition = (playerPosition + 5 + step) % 5
    checkPlayerPosition(board)

def movement(board:  List[List[str]]) -> None:
    """Checks if the player pressed a button and moves him accordingly

    Args:
        board (List[List[str]]): The current board
    """
    if button_a.is_pressed():
        movePlayer(board, -1)
    if button_b.is_pressed():
        movePlayer(board, 1)

def checkPlayerPosition(board: List[List[str]]) -> None:
    """Checks if the plyaer is on a block, if yes it displays a Game Over screen

    Args:
        board (List[List[str]]): the given board
    """
    if board[4][playerPosition] != "":
        gameOver()

def waitForStart() -> None:
    """Waits until the player wants to start a game"""
    display.scroll("Start?")
    display.show(Image.ARROW_W)
    while True:
        if button_a.is_pressed():
            display.clear()
            sleep(150)
            return
        sleep(100)

def gameOver() -> None:
    """Displays the Game Over screen, current points and current high score"""
    global gameOverVar, maxScore
    gameOverVar = True
    if playerScore > maxScore:
        maxScore = playerScore
    display.show("GAME OVER")
    display.scroll("Your score: " + str(playerScore) + ", Record: " + str(maxScore), delay=90)

def generateLine() -> List[str]:
    """Generates a new Line with a random block

    Returns:
        List(str): A new line for the game, with a random new block
    """
    tmp = ["","","","",""]
    randNum = random.randint(0, 4)
    tmp[randNum] = "B"
    return tmp

def moveDown(board: List[List[str]]) -> None:
    """Moves the given board a line down, and generates a new line on top

    Args:
        board (List[List[str]]): The given board
    """
    board.insert(0, generateLine())
    del board[len(board) - 1]
    checkPlayerPosition(board)

def checkLevel() -> None:
    """Increseas the playerLevel if needed"""
    if playerScore % 10 == 0:
        increaseLevel()

def increaseLevel() -> None:
    """Increases the players level"""
    global playerLevel
    if playerLevel < maxLevel:
        playerLevel += 1

def main() -> None:
    """Main Game Loop"""
    global gameOverVar, playerPosition, playerScore, playerLevel
    while True:
        gameOverVar = False
        playerPosition = 2
        playerScore = 0
        playerLevel = 0
        board = generateBoard()
        waitForStart()
        while not gameOverVar:
            # TODO: fix loop bug when crash on index = 0
            for index in range(10 - playerLevel):
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
