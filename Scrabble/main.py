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

def genHand():
    # Each player has 7 chips
    A = {
        "A": 1
        }
    B = {
        "B": 3
        }
    C = {
        "C": 3
        }
    D = {
        "D": 2
        }
    E = {
        "E": 1
        }
    F = {
        "F": 4
        }
    G = {
        "G": 2
        }
    H = {
        "H": 4
        }
    I = {
        "I": 1
        }
    J = {
        "J": 8
        }
    K = {
        "K": 5
        }
    L = {
        "L": 1
        }
    M = {
        "M": 3
        }
    N = {
        "N": 1
        }
    O = {
        "O": 1
        }
    P = {
        "P": 3
        }
    Q = {
        "Q": 10
        }
    R = {
        "R": 1
        }
    S = {
        "S": 1
        }
    T = {
        "T": 1
        }
    U = {
        "U": 1
        }
    V = {
        "V": 4
        }
    W = {
        "W": 4
        }
    X = {
        "X": 8
        }
    Y = {
        "Y": 4
        }
    Z = {
        "Z": 10
        }

def main():
    genHand()


if __name__ == "__main__":
    main()










