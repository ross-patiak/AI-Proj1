from random import randint
import matplotlib.pyplot as plt 

def main():
    board, size = build_GUI()
    hill_climb(board, size)

    
def hill_climb(board, size):
    x_vals = [(i+1) for i in range(50)]
    y_vals = []
    rand_celly = size-1
    rand_cellx= size-1

    while rand_cellx == size-1 and rand_celly == size-1:
        rand_cellx = randint(0, size-1)
        rand_celly = randint(0, size-1)
    
    print(rand_cellx)
    print(rand_celly)


    # for i in range(x_vals):
    #     for j in range(i):
    #         answer = i
    #     y_vals.append()

    

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
    
    return (grid, grid_size)


if __name__=='__main__':
    main()