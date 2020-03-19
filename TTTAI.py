# Tic Tac Toe game in Python with AI

grid = [' ' for x in range(10)]

def insertCharacter(character, pos):
	grid[pos] = character

def spaceIsFree(pos):
	return grid[pos] == ' '

def printGrid(grid):
	print('   |   |')
	print(' ' + grid[1] + ' | ' + grid[2] + ' | ' + grid[3])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + grid[4] + ' | ' + grid[5] + ' | ' + grid[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + grid[7] + ' | ' + grid[8] + ' | ' + grid[9])
	print('   |   |')

def isWinner(grid, character):
	return (grid[7] == character and grid[8] == character and grid[9] == character) or (grid[4] == character and grid[5] == character and grid[6] == character) or (grid[1] == character and grid[2] == character and grid[3] == character) or (grid[1] == character and grid[4] == character and grid[7] == character) or (grid[2] == character and grid[5] == character and grid[8] == character) or (grid[3] == character and grid[6] == character and grid[9] == character) or (grid[1] == character and grid[5] == character and grid[9] == character) or (grid[7] == character and grid[5] == character and grid[3] == character) 

def playerMove():
	run = True
	while run:
		move = input('Please select a position to place your \'X\' (1-9): ')
		try:
			move = int(move) # make sure input is an integer
			if move > 0 and move < 10: # make sure input is a valid number
				if spaceIsFree(move):
					run = False
					insertCharacter('X', move)
				else:
					print('Space is already taken!')
			else:
				print('Please insert a valid position (1-9)')
		except:
			print('Please type a number (1-9)!')

def aiMove():
	# 5 step algorithm

	# Creating a list of possible moves for the AI
	possibleMoves = [x for x, character in enumerate(grid) if character == ' ' and x != 0]
	move = 0

	# First, check to see if AI can win or block player from winning
	for let in ['O', 'X']:
		for i in possibleMoves:
			gridCopy = grid[:]
			gridCopy[i] = let
			if isWinner(gridCopy, let):
				move = i
				return move

	# Second, attempt to take a corner
	cornersOpen = []
	for i in possibleMoves:
		if i in [1,3,7,9]:
			cornersOpen.append(i)
		if len(cornersOpen) > 0:
			move = selectRandom(cornersOpen)
			return move

	# Third, attempt to take the center 
	if 5 in possibleMoves:
		move = 5
		return move

	# Fourth, try to take any edge
	edgesOpen = []
	for i in possibleMoves:
		if i in [2,4,6,8]:
			edgesOpen.append(i)
		if len(edgesOpen) > 0:
			move = selectRandom(edgesOpen)

	return move



def selectRandom(li):
	import random
	ln = len(li)
	r = random.randrange(0, ln)
	return li[r]


def isGridFull(grid):
	if grid.count(' ') > 1:
		return False
	else:
		return True


def main():
	print('Tic Tac Toe! by Jacob Duncan')
	print('AI: O | You: X' )
	print('Have fun and enjoy the game!')
	printGrid(grid)

	while not(isGridFull(grid)):
		if not(isWinner(grid, 'O')):
			playerMove()
			printGrid(grid)
		else:
			print('Sorry, the AI won this time!')
			break

		if not(isWinner(grid, 'X')):
			move = aiMove()
			if move == 0:
				print('Tie Game!')
			else:
				insertCharacter('O', move)
				print('AI placed an \'O\' in position', move)
				printGrid(grid)
		else:
			print('Congrats, you won!')
			break



if isGridFull(grid):
			print('Tie Game!')


#
#while True:
#	answer = input('Would you like to play again? (y/n)')
#	if answer.lower() == 'y' or answer.lower() == 'n':
#		grid = [' ' for x in range(10)]
#		print('-----------------------------------')
#		main()
#	else:
#		break

main()
