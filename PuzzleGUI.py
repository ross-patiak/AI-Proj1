from random import randint

def build_GUI():
    valid_sizes = [5, 7, 9, 11]
    grid_size = 0

    while grid_size not in valid_sizes:
        print('Pick a puzzle grid size: 5, 7, 9, or 11')
        grid_size = input()

    grid = [[0] * grid_size for i in range(grid_size)]

    for i in range(grid_size):
        for j in range(grid_size):
            if i == grid_size-1 and j == grid_size-1:
                break
            else:
                max_move = max(grid_size - (i+1), i, grid_size - (j+1), j)
                grid[i][j] = randint(1, max_move)

    print(grid)


if __name__=='__main__':
    build_GUI()
