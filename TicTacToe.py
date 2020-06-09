# Tic Tac Toe

import random, copy

def drawBoard(board):
    # This Function prints out the board that it was passed.

    # 'Board' is a list of 10 strings represting the board (ignore index 0)
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def inputPlayerLetter():
    # Let's the player type which letter they want to be.
    # Returns a list with the player's letter as the first item and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    
    # The first element in the tuple is the player's letter, the second in computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type too much.
    return ((bo['top-L'] == le and bo['top-M'] == le and bo['top-R'] == le) or # Across the top
           (bo['mid-L'] == le and bo['mid-M'] == le and bo['mid-R'] == le) or # Accross the middle
           (bo['low-L'] == le and bo['low-M'] == le and bo['low-R'] == le) or # Across the bottom
           (bo['top-L'] == le and bo['mid-L'] == le and bo['low-L'] == le) or # Down the left side
           (bo['top-M'] == le and bo['mid-M'] == le and bo['low-M'] == le) or # Down the middle
           (bo['top-R'] == le and bo['mid-R'] == le and bo['low-R'] == le) or # Down the right side 
           (bo['top-L'] == le and bo['top-M'] == le and bo['top-R'] == le) or # diagonal
           (bo['top-R'] == le and bo['mid-M'] == le and bo['low-L'] == le)) # diagonal

def isSpaceFree(board, move):
    # Returns True if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # let the Player type in his move.
    move = ' '
    while move not in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split() or not isSpaceFree(board, move):
        print('What is your next move? (top-, mid-, low- | L, M, R)')
        move = input()
    return move

def chooseRandomMoveFromList(board, moveList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
        
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determne where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i):
            makeMove(dupe, computerLetter, i)
            if isWinner(dupe, computerLetter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i):
            makeMove(dupe, playerLetter, i)
            if isWinner(dupe, computerLetter):
                return i
    
    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, ['top-L', 'top-R', 'low-L', 'low-R'])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 'mid-M'):
        return 'mid-M'

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, ['top-M', 'low-M', 'mid-L', 'mid-R'])

def isBoardFull(board):
    # Returns True if every space on the board has been taken. othersise return False.
    for i in 'top-L top-M top-R mid-L mid-M mid-R low-L low-M low-R'.split():
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board 
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's Turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a Tie!')
                    break
                else:
                    turn = 'computer'
        

        else:
            # Computer's Turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The game is a Tie!')
                break
            else:
                turn = 'player'

    if not playAgain():
        break