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

def spaceIsFree(position):
    return board[position] == ' '

def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def checkForWin():
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [7, 5, 3]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != ' ':
            return True
    return False

def checkWhichMarkWin(mark):
    win_conditions = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [7, 5, 3]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] == mark:
            return True
    return False

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print("Draw!")
            exit()

        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
            else:
                print("Player wins!")
            exit()
    else:
        print("Position already occupied. Choose another position.")
        position = getValidPosition("Enter a valid position: ")
        insertLetter(letter, position)

def getValidPosition(prompt):
    while True:
        try:
            position = int(input(prompt))
            if position in range(1, 10):
                return position
            else:
                print("Position must be between 1 and 9.")
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 9.")

player = 'O'
bot = 'X'

def playerMove():
    position = getValidPosition("Enter the position for 'O': ")
    insertLetter(player, position)

def minimax(board, depth, isMaximizing, alpha, beta):
    if checkWhichMarkWin(bot):
        return 10 - depth
    elif checkWhichMarkWin(player):
        return depth - 10
    elif checkDraw():
        return 0

    if isMaximizing:
        maxEval = -float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[key] = ' '
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return maxEval
    else:
        minEval = float('inf')
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[key] = ' '
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return minEval

def compMove():
    bestScore = -float('inf')
    bestMove = -1

    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, 0, False, -float('inf'), float('inf'))
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    insertLetter(bot, bestMove)

while not checkForWin():
    compMove()
    playerMove()