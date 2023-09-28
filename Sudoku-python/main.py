'''
Assigning values to the grid
The grid will look like this:
  0,0 | 0,1 | 0,2 | 0,3 | 0,4 | 0,5 | 0,6 | 0,7 | 0,8
  1,0 | 1,1 | 1,2 | 1,3 | 1,4 | 1,5 | 1,6 | 1,7 | 1,8
  2,0 | 2,1 | 2,2 | 2,3 | 2,4 | 2,5 | 2,6 | 2,7 | 2,8
  3,0 | 3,1 | 3,2 | 3,3 | 3,4 | 3,5 | 3,6 | 3,7 | 3,8
  4,0 | 4,1 | 4,2 | 4,3 | 4,4 | 4,5 | 4,6 | 4,7 | 4,8
  5,0 | 5,1 | 5,2 | 5,3 | 5,4 | 5,5 | 5,6 | 5,7 | 5,8
  6,0 | 6,1 | 6,2 | 6,3 | 6,4 | 6,5 | 6,6 | 6,7 | 6,8
  7,0 | 7,1 | 7,2 | 7,3 | 7,4 | 7,5 | 7,6 | 7,7 | 7,8
  8,0 | 8,1 | 8,2 | 8,3 | 8,4 | 8,5 | 8,6 | 8,7 | 8,8
'''
import random
N = 9
root_N = int(N ** 0.5)
grid = [[0 for x in range(N)] for y in range(N)]
cpy_grid = [[0 for x in range(N)] for y in range(N)]


#This function prints the grid of 2048 Game as the game progresses
def print_grid():
    dd_len = len(str(N))
    print(('-' * (N*(dd_len+2))) + ('---' * root_N) + '-')
    for i in range(N):
        print(end='|  ')
        for j in range(N):
            if j % root_N == 0 and j > 0:
                print('|  ', end='')
            if grid[i][j] == 0:
                print('.'*dd_len, end='  ')
            else:
                print('0'*(dd_len - len(str(grid[i][j]))) + str(grid[i][j]), end='  ')
        print(end='|')
        print()
        if i % root_N == root_N - 1:
            print(('-' * (N*(dd_len+2))) + ('---' * root_N) + '-')

#This function checks if all rows and columns and boxes is full with all numbers
def check_win():
    num=0
    for i in range (N):
        for j in range (N):
            if grid[i][j] !=0:
                num=num+1
    if num == 81 :
        return True
    else :
        return False

#This function checks if given position is valid or not
def check_valid_position(i, j):
    if i < len(grid) and j < len(grid):
        return True
    else:
        return False

#This function checks if given cell is empty or not
def check_empty_cell(i, j):
    if grid[i][j] == 0:
        return True
    else:
        return False

#This function checks if given cell is original or not
def check_original_cell(i, j):
    if cpy_grid[i][j] != 0:
        return True
    else:
        return False

#This function checks if the given cell is valid with the given numbers
def check_valid_value(i, j, v):
    count_x = 0
    count_y = 0
    if v == 0:
        set_cell(i, j ,v)
        return True
    if v < 0 or v > 9:
        return False
    #check valid row
    for x in range(0, N):
        if grid[i][x] != v and x != j:
            count_x += 1
    if count_x == 8:
        #check valid column
        for y in range(0, N):
            if grid[y][j] != v and y != i:
                count_y += 1

    if count_y == 8:
        for r in range (3):
            for c in range (3):
                if(grid[r + (i-(i % 3))][c + (j-(j % 3))] == v):
                    return False

        return True


#This function sets a value to a cell
def set_cell(i, j, v):
    grid[i][j] = v

#This function solve the grid
def solve_grid(i, j):
    if j == N:
        i += 1
        j = 0
    if i == N:
        return True
    if check_original_cell(i, j):
        return solve_grid(i, j + 1)
    for k in range(1, N+1):
        if check_valid_value(i, j, k):
            grid[i][j] = k
            cpy_grid[i][j] = k
            if solve_grid(i, j + 1):
                return True
        grid[i][j] = 0
        cpy_grid[i][j] = 0
    return False

#This function generates cells in the grid
def generate_cells():
    #Generate cells in the diagonal boxes of the grid
    for k in range(0, N, root_N):
        for i in range(root_N):
            for j in range(root_N):
                n = random.randint(1, N+1)
                while not check_valid_value(k+i, k+j, n) or check_original_cell(k+i, k+j):
                    n = random.randint(1, N+1)
                grid[k+i][k+j] = n
                cpy_grid[k+i][k+j] = n
    #Solve the complete grid
    solve_grid(0, 0)
    #Remove cells in the grid to be solved
    prev_x, prev_y = 0, 0
    for k in range(N*N - N//2*N):
        i = (random.randint(0, N-1) + prev_x + root_N) % N
        j = (random.randint(0, N-1) + prev_y + root_N) % N
        while not check_original_cell(i, j):
            i = (random.randint(0, N-1) + prev_x + root_N) % N
            j = (random.randint(0, N-1) + prev_y + root_N) % N
        grid[i][j] = 0
        cpy_grid[i][j] = 0
        prev_x, prev_y = i, j

#This function clears the grid
def grid_clear():
    i = 0
    for x in grid:
        j = 0
        for y in x:
            grid[i][j] = 0
            j += 1
        i += 1




#MAIN FUNCTION
def play_game():
    print("Sudoku Game!")
    print("Welcome...")
    print("============================")
    while True:
        #Prints the grid
        print_grid()
        #Read an input from the player
        i, j, v = map(int, input('Enter the position and value: ').split())
        while not check_valid_position(i, j) or not check_valid_value(i, j, v) or check_original_cell(i, j):
            i, j, v = map(int, input('Enter a valid position and value: ').split())
        #Set the input position with the value
        set_cell(i, j, v)
        #Check if the state of the grid has a win state
        if check_win():
            #Prints the grid
            print_grid()
            print('Congrats, You won!')
            break

while True:
    grid_clear()
    generate_cells()
    play_game()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break
