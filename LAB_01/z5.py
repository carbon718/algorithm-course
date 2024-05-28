# x = 1
# o = -1
import random

def main():

    with_computer_str = input('Do you want to play with a computer? (y) ')
    with_computer = False
    if with_computer_str == 'y':
        with_computer = True

    moveNumber = 1
    currentPlayer = random.choice([-1, 1])
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while checkIfGameEnded(board) == 0:
        if(with_computer and currentPlayer == -1):
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            while not isValidMove(board, row, column):
                row = random.randint(0, 2)
                column = random.randint(0, 2)
            board[row][column] = currentPlayer
            currentPlayer = -currentPlayer
            moveNumber += 1
            continue
        printBoard(board)
        print("Enter row and column, player", znak(currentPlayer))
        row = int(input('Row:'))
        column = int(input('Column:'))
        while not isValidMove(board, row, column):
            print("Invalid move")
            row = int(input('Row? '))
            column = int(input('Column? '))
        board[row][column] = currentPlayer
        currentPlayer = -currentPlayer
        if moveNumber == 9:
            printBoard(board)
            print("Draw")
            break
        moveNumber += 1




def isValidMove(board, row, column):
    if row < 0 or row > 2 or column < 0 or column > 2:
        return False
    if board[row][column] != 0:
        return False
    return True

def checkIfGameEnded(board):
    for i in range(3):
        sumRow = board[i][0] + board[i][1] + board[i][2]
        sumColumn = board[0][i] + board[1][i] + board[2][i]
        if sumRow == 3 or sumColumn == 3:
            printBoard(board)
            print(znak(1), "won")
            return 1
        elif sumRow == -3 or sumColumn == -3:
            printBoard(board)
            print(znak(-1), "won")
            return -1
    if(board[0][0] + board[1][1] + board[2][2] == 3 or board[0][2] + board[1][1] + board[2][0] == 3):
        printBoard(board)
        print(znak(1), "won")
        return 1
    elif (board[0][0] + board[1][1] + board[2][2] == -3 or board[0][2] + board[1][1] + board[2][0] == -3):
        printBoard(board)
        print(znak(-1), "won")
        return -1
    return 0

def printBoard(board):
    print_line()
    for i in range(3):
        print('| ', end='')
        for j in range(3):
            print(znak(board[i][j]), end='')
            print_spacer()
        print()
        print_line()

def print_line():
    for i in range(12):
        print('-', end='')
    print('-')

def print_spacer():
    print(' | ', end='')

def znak(liczba):
    if liczba == -1:
        return "o"
    elif liczba == 1:
        return "x"
    else:
        return " "


if __name__ == '__main__':
    main()
