import numpy as np
import random
from time import sleep

def createBoard():
    return(np.array([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))



#check for empty places on board

def possibilities(board):
    l = []

    for i in range(len(board)):
        for j in range(len(board)):

            if board[i][j] == 0:
                l.append((i, j))
    return(l)

#select a random spot
def randomSpot(board, player):
    spot = possibilities(board)
    current_loc = random.choice(spot)
    print("Spot:" +str(current_loc))
    board[current_loc] = player
    return (board)


#check if horizontal win
def isHorizontalWin(board, player):
    for i in range(len(board)):
        win = True

        for j in range(len(board)):
            if board[i][j] != player:
                win = False
                continue

    if win == True:
        return (win)


#check if vertical win
def isVerticalWin(board, player):
    for i in range(len(board)):
        win = True

        for j in range(len(board)):
            if board[j][i] != player:
                win = False
                continue

    if win == True:
        return (win)


#check if diagonal win
def isDiagonalWin(board, player):
    win = True

    for i in range(len(board)):
            if board[i][i] != player:
                win = False
                continue

    if win == True:
        return (win)


def evaluateBoard(board):

    winner = 0

    for player in [1,2]:
        if (isVerticalWin(board, player)) or (isHorizontalWin(board, player)) or (isDiagonalWin(board, player)):
            return (player)

    if np.all(board != 0) and winner == 0:
        winner = -1

    return winner


def playGame():

    board = createBoard()

    print(board)

    winner,counter = 0,1
    sleep(2)

    while winner == 0:
        for player in [1, 2]:
            board = randomSpot(board, player)
            print("Board after " + str(counter) + " move")
            print(board)
            sleep(2)
            counter += 1
            winner = evaluateBoard(board)
            if winner != 0:
                break
    return(winner)


print("Winner of the game is: " +str(playGame()))







