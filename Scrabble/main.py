grid = [' ' for x in range(225)]

def insertChip(chip, pos):
    # Need to check if this is valid tho
    # Also need to show a "Thinking" state
    # Where the player can insert and take out
    # Chips to see what works best to play
    grid[pos] = chip

# Used to input validate placement of chips
def isSpaceFree(pos):
    if grid[pos] == ' ':
        return true
    else:
        return false

# Used to print the board at any current moment
# in the game
def printBoard(grid):
    for i in range(225):
        if i % 15 == 0:
            print(grid[i])
            print()
        else:
            print(grid[i], " ")









