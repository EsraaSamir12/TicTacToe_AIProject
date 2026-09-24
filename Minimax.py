import random  # to make the computer play randomly
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' ',
}

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')

def isFree(position):
    if(board[position] == ' '):
        return True
    else:
        return False

def checkForDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def checkForWin():
    win_stats = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [7, 5, 3]
    ]
    for stat in win_stats:
        if board[stat[0]] == board[stat[1]] == board[stat[2]] and board[stat[0]] != ' ':
            return True
    return False

def checkWhichMarkWin(mark):
    win_stats = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [7, 5, 3]
    ]
    for stat in win_stats:
        if board[stat[0]] == board[stat[1]] == board[stat[2]] and board[stat[0]] == mark:
            return True
    return False

def insertLetter(letter, position):
    if position < 1 or position > 9:
        position = getValidPosition("Enter a valid position (1-9): ")
        insertLetter(letter, position)
        return False

    if isFree(position):
        board[position] = letter
        printBoard(board)
        if(checkForDraw()):
            print("Draw!")
            exit()

        if checkForWin():
            if letter == 'X':
                print("Computer wins!")
                exit()
            else:
                print("You win!")
                exit()
                return

    else:
        print("Position already occupied.")
        position = getValidPosition("Choose another position: ")
        insertLetter(letter, position)
        return False

def getValidPosition(prompt):
    while True:
        try:
            position = int(input(prompt))
            return position
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 9.")

player = 'O'
bot = 'X'

def playerMove():
    position = getValidPosition("Enter the position for 'O': ")
    insertLetter(player, position)
    return

def minimax(board, isMaximizing):
    if checkWhichMarkWin(bot):
        return 1
    elif checkWhichMarkWin(player):
        return -1
    elif checkForDraw():
        return 0

    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore
    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore

def compMore():  
    if all(space == ' ' for space in board.values()):  
        firstMove = random.choice(list(board.keys()))  
        insertLetter(bot, firstMove)  
        return  

    bestScore = -1000  
    bestMove = -1  
    for key in board.keys():  
        if board[key] == ' ':  
            board[key] = bot  
            score = minimax(board, False)  
            board[key] = ' '  
            if score > bestScore:  
                bestScore = score  
                bestMove = key  
    insertLetter(bot, bestMove) 
    
while not checkForWin():
    compMore()
    playerMove()