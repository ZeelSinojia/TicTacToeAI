import random

XPLAYER = +1
OPLAYER = -1
EMPTY = 0

board = [' '] * 9
winning_condition = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def clearBoard(board):
	board = [' '] * 9

def printBoard(board):
	print('\n')
	print(board[0] + ' | ' + board[1] + ' | ' + board[2] + '\t0 | 1 | 2')
	print('----------')
	print(board[3] + ' | ' + board[4] + ' | ' + board[5] + '\t3 | 4 | 5')
	print('----------')
	print(board[6] + ' | ' + board[7] + ' | ' + board[8] + '\t6 | 7 | 8')
	print('\n')

def isBoardFull(board):
	if len(emptyCells(board)) == 0:
		return True
	return False

def emptyCells(board):
	empty = []
	for i in range(9):
		if board[i] == ' ':
			empty.append(i)
	return empty

def isGameWon(board):
	if isWinningPlayer(board, XPLAYER) or isWinningPlayer(board, OPLAYER):
		return True
	return False

def isWinningPlayer(board, player):
	if player == XPLAYER:
		p = 'X'
		for w in winning_condition:
			if board[w[0]] == board[w[1]] == board[w[2]] == p:
				return True
	else:
		p = 'O'
		for w in winning_condition:
			if board[w[0]] == board[w[1]] == board[w[2]] == p:
				return True
	return False

def printResult(board):
	if isWinningPlayer(board, XPLAYER):
		print('X won\n')
	elif isWinningPlayer(board, OPLAYER):
		print('O won\n')
	else:
		print('Draw\n')

def changePlayer(player):
	if player == XPLAYER:
		return OPLAYER
	return XPLAYER

def XplayerMove(board):
	e = True
	while e:
		move = int(input('Pick a position(0-8)'))
		if move not in emptyCells(board):
			print('Location filled')
		else:
			setMove(board,move,XPLAYER)
			printBoard(board)
			e = False

def OplayerMove(board):
	e = True
	while e:
		move = int(input('Pick a position(0-9)'))
		if move not in emptyCells(board):
			print('Location filled')
		else:
			setMove(board,move,OPLAYER)
			printBoard(board)
			e = False	

def setMove(board, move, player):
	if player == XPLAYER:
		board[move] = 'X'
	elif player == OPLAYER:
		board[move] = 'O'
	elif player == EMPTY:
		board[move] = ' '

def MiniMax(board, depth, player):

	if depth == 0 or isGameWon(board):
		if isWinningPlayer(board, XPLAYER):
			return 0
		elif isWinningPlayer(board, OPLAYER):
			return 100
		else:
			return 50

	if player == XPLAYER:
		bestValue = 100
		for move in emptyCells(board):
			setMove(board, move, player)
			score = MiniMax(board, depth - 1, -player)
			setMove(board, move, EMPTY)
			bestValue = max(bestValue, score)
		return bestValue

	if player == OPLAYER:
		bestValue = 0
		for move in emptyCells(board):
			setMove(board, move, player)
			score = MiniMax(board, depth - 1, -player)
			setMove(board, move, EMPTY)
			bestValue = max(bestValue, score)
		return bestValue

def AIMove(board, depth, player):
	neutralValue = 50
	choices = []
	for move in emptyCells(board):
		setMove(board, move, player)
		moveValue = MiniMax(board, depth-1, -player)
		setMove(board, move, EMPTY)
	
		if moveValue > neutralValue:
			choices = [move]
			break
		elif moveValue == neutralValue:
			choices.append(object)
	
	if len(choices) > 0:
		return random.choice(choices)
	else:
		return random.choice(emptyCells(board))

def makeMove(board, player, mode = 1):
	if mode == 1:
		if player == XPLAYER:
			XplayerMove(board)
		else:
			ai_move = AIMove(board, -1, player)
			setMove(board, ai_move, player)
			printBoard(board)
	else:
		if player == XPLAYER:
			XplayerMove(board)
		else:
			OplayerMove(board)


def playerVsAI():
	order = int(input('Would you like to go first or second?(1/2)'))
	
	clearBoard(board)
	if order == 2:
		currentPlayer = OPLAYER
	else:
		currentPlayer = XPLAYER

	while True:
		if not (isBoardFull(board) or isGameWon(board)):
			makeMove(board, currentPlayer)
			currentPlayer *= -1
		else:
			break
	printResult(board)

def playerVsPlayer():
	print('X will go first')

	clearBoard(board)
	currentPlayer = XPLAYER
	while True:
		if not (isBoardFull(board) or isGameWon(board)):
			makeMove(board, currentPlayer, mode = 2)
			currentPlayer *= -1
		else:
			break
	printResult(board)

def main():
	mode = int(input('Player vs AI or Player vs Player(1/2)'))
	if mode == 1:
		playerVsAI()
	else:
		playerVsPlayer()

main()