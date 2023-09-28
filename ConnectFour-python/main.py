'''
Assigning values to the grid
The grid will look like this:
  0,0 | 0,1 | 0,2 | 0,3 | 0,4 | 0,5 | 0,6
  1,0 | 1,1 | 1,2 | 1,3 | 1,4 | 1,5 | 1,6
  2,0 | 2,1 | 2,2 | 2,3 | 2,4 | 2,5 | 2,6
  3,0 | 3,1 | 3,2 | 3,3 | 3,4 | 3,5 | 3,6
  4,0 | 4,1 | 4,2 | 4,3 | 4,4 | 4,5 | 4,6
  5,0 | 5,1 | 5,2 | 5,3 | 5,4 | 5,5 | 5,6
'''
N, M = 6, 7
grid = [['.' for x in range(M)] for y in range(N)]

#This function prints the grid of Connect Four Game as the game progresses
def print_grid():
    print("Player 1: X  vs  Player 2: O")
    print('--' + '---' * M + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(M):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * M + '--')

#This function checks if row or column or diagonal is full with same characters
def check_win():
    height = len(grid[0])
    width = len(grid)

    #columns
    for x in range(width):
        for y in range(height - 3):
            if grid[x][y] == grid[x][y+1] == grid[x][y+2] == grid[x][y+3] and grid[x][y] != '.':
                return True

    #rows
    for y in range(height):
        for x in range(width - 3):
            if grid[x][y] == grid[x+1][y] == grid[x+2][y] == grid[x+3][y] and grid[x][y] != '.':
                return True

    #diagonals
    for x in range(width - 3):
        for y in range(3, height):
            if grid[x][y] == grid[x + 1][y - 1] == grid[x + 2][y - 2] == grid[x + 3][y - 3] and grid[x][y] != '.':
                return True

        # check \ diagonal spaces
    for x in range(width - 3):
        for y in range(height - 3):
            if grid[x][y] == grid[x + 1][y + 1] == grid[x + 2][y + 2] == grid[x + 3][y + 3] and grid[x][y] != '.':
                return True


#This function checks if row or column or diagonal is full with same characters
def check_tie(mark):
    x_num, o_num = 0, 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'X':
                x_num = x_num + 1
            if grid[i][j] == 'O':
                o_num = o_num + 1
    if o_num + x_num == 42 and not check_win():
        return True
    else:
        return False


    #This function checks if given cell is empty or not
def check_empty(i):
    j=5   #num of rows
    for x in grid:
        if grid[j][i] != '.':
            j=j-1
        else:
            return True
            break


#This function checks if given position is valid or not
def check_valid_column(i):
    if i <= len(grid):
        return True
    else:
        return False

#This function sets a value to a cell
def set_cell(i, mark):
    j=5
    for x in grid:
        if grid[j][i] != '.':
            j=j-1
        else:
            grid[j][i]=mark
            break

#This function clears the grid
def grid_clear():
    i = 0
    for x in grid:
        j = 0
        for y in x:
            grid[i][j] = '.'
            j += 1
        i += 1

#MAIN FUNCTION
def play_game():
    print("Connect Four Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        #Prints the grid
        print_grid()
        #Set mark value based on the player
        mark = 'X' if player == 0 else 'O'
        #Takes input from the user to fill in the grid
        print('Player %s' % mark)
        i = int(input('Enter the column index: '))
        while not check_valid_column(i) or not check_empty(i):
            i = int(input('Enter a valid column index: '))
        #Set the input position with the mark
        set_cell(i, mark)
        #Check if the state of the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            print('Congrats, Player %s is won!' % mark)
            break
        op_mark = 'O' if player == 0 else 'X'
        #Check if the state of the grid has a tie state
        if check_tie(op_mark):
            #Prints the grid
            print_grid()
            print("Woah! That's a tie!")
            break
        #Player number changes after each turn
        player = 1 - player


while True:
	grid_clear()
	play_game()
	c = input('Play Again [Y/N] ')
	if c not in 'yY':
		break