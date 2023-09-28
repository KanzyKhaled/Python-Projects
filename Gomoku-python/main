N, M = 15, 15
a_row = 5
n_players = 2
marks = ['X', 'O']
grid = [['.' for x in range(N)] for y in range(M)]
win_N = 5


# This function prints the grid of Gomoku as the game progresses
def print_grid():
    for i in range(n_players):
        print('Player %d: %c  ' % (i + 1, marks[i]), end='')
        if i < n_players - 1:
            print('vs  ', end='')
    print()
    print('--' + '---' * M + '--')
    for i in range(N):
        print(end='|  ')
        for j in range(M):
            print(grid[i][j], end='  ')
        print(end='|')
        print()
        print('--' + '---' * M + '--')


# This function checks if the game has a win state or not
def check_win():
    i, j, count = 0, 0, -2
    # rows
    for i in range(N):
        for j in range(M-1):
            if grid[i][j] == grid[i][j+1] and grid[i][j] != '.':
                count += 1
                if count == win_N:
                    return True

    # columns
    i, j, count = 0, 0, -2
    for i in range(N):
        for j in range(M-1):
            if grid[j][i] == grid[j+1][i] and grid[j][i] != '.':
                count += 1
                if count == win_N:
                    return True

    # diagonals
    #---\\\\-------
    i, j, count = 0, 0, 1
    for i in range(N):
        for j in range(M-1):
            if i == j and grid[i][j] == grid[i+1][j+1] and grid[i][j] != '.':
                count += 1
                if count == win_N:
                    return True
    #---////-------
    i, j, count = 0, 0, 1
    for i in range(N-1):
        if grid[i][(N-1)-i] == grid[i+1][(N-1)-(i+1)] and grid[i][(N-1)-i] != '.':
            count += 1
            if count == win_N:
                return True
    return False

# This function checks if the game has a tie state or not for the given mark
def check_tie_player(mark):
    #rows
    count = 0
    for i in range(N):
        for j in range(M-4):
            for x in range(win_N):
                if grid[i][j] == '.' or grid[i][j] == mark and grid[i][j+x] == mark or grid[i][j+x] == '.':
                  count += 1
        if count >= win_N:
            return False

    #columns
    count = 0
    for i in range(N):
        for j in range(M - 4):
            for x in range(win_N):
                if grid[j][i] == '.' or grid[j][i] == mark and grid[j+x][i] == mark or grid[j+x][i] == '.':
                   count += 1
        if count >= win_N:
            return False


    #diagonals
    #----\\\-----
    count = 0
    for i in range(N):
        for j in range(M-4):
            if i == j:
                for x in range(win_N):
                    if grid[i][j] == '.' or grid[i][j] == mark and grid[i+x][j+x] == mark or grid[i+x][j+x] == '.':
                       count += 1
        if count >= win_N:
            return False

    #----///-----
    count = 0
    for i in range(N-1):
        for x in range(win_N):
            if grid[i][(N-1)-i] == mark or grid[i][(N-1)-i] == '.' and grid[i+x][(N-1)-(i+x)] == mark or grid[i+x][(N-1)-(i+x)] == '.':
                count += 1
    if count >= win_N:
        return False


    return True

# This function checks if the game has a tie state or not
def check_tie():
    all_tie = True
    for mark in marks:
        if not check_tie_player(mark):
            all_tie = False
    return all_tie


# This function checks if given cell is empty or not
def check_empty(i, j):
    if grid[i][j] == '.':
        return True
    else:
        return False


# This function checks if given position is valid or not
def check_valid_position(i, j):
    if -1 < i < N and -1 < j < M:
        return True
    else:
        return False


# This function sets the given mark to the given cell
def set_cell(i, j, mark):
    grid[i][j] = mark


# This function clears the game structures
def grid_clear():
    for i in range(N):
        for j in range(N):
            grid[i][j] = '.'


# This function reads a valid position input
def read_input():
    i, j = map(int, input('Enter the row index and column index: ').split())
    while not check_valid_position(i, j) or not check_empty(i, j):
        i, j = map(int, input('Enter a valid row index and a valid column index: ').split())
    return i, j


# MAIN FUNCTION
def play_game():
    print("Gomoku Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        # Prints the grid
        print_grid()
        # Read an input position from the player
        print('Player %s is playing now' % marks[player])
        i, j = read_input()
        # Set the player mark in the input position
        set_cell(i, j, marks[player])
        # Check if the grid has a win state
        if check_win():
            # Prints the grid
            print_grid()
            # Announcement of the final statement
            print('Congrats, Player %s is won!' % marks[player])
            break
        # Check if the grid has a tie state
        if check_tie():
            # Prints the grid
            print_grid()
            # Announcement of the final statement
            print("Woah! That's a tie!")
            break
        # Player number changes after each turn
        player = (player + 1) % n_players
print(list(range(N)))

while True:
    grid_clear()
    play_game()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break
