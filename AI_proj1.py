import os
import sys
import queue
from random import randint
import matplotlib.pyplot as plt 


def main():
    board, size = build_GUI()
    x = evaluate(board, size)
    pboard(x[0], size, x[1])
    hill_climb(board, size)


def hill_climb(board, size):
    x_vals = [(i+1) for i in range(200)]
    y_vals = []
    rand_y = size-1
    rand_x = size-1
    valfunc_og = evaluate(board, size)[1]
    valfunc_max = valfunc_og

    for i in range(len(x_vals)):
        #does this belong here? (are we modifying the og board everytime?)
        new_board = board

        for j in range(i+1):
            #pick random cell
            while True:
                rand_x = randint(0, size-1)
                rand_y = randint(0, size-1)

                if rand_x != size-1 and rand_y != size-1:
                    break

            #max legal move for that random cell
            max_move = max(size - (rand_x+1), rand_x, size - (rand_y+1), rand_y)
            old_cell = board[rand_x][rand_y]
            
            #change cell then find new value function
            new_board[rand_x][rand_y] = randint(1, max_move)
            valfunc_new = evaluate(new_board, size)[1]

            #if new val func > current max val func found so far, change max
            #capture that new board to visualize later
            if valfunc_new < valfunc_og:
                new_board[rand_x][rand_y] = old_cell
            elif valfunc_new > valfunc_max:
                valfunc_max = valfunc_new
                final_board = new_board


        y_vals.append(valfunc_max)
    
    print('--------------------------')
    print('Hill Climb Result:')
    for i in range(size):
        print(final_board[i])
    print('value function is: ' + str(valfunc_max))

    plt.plot(x_vals, y_vals)
    plt.xlabel('number of iterations')
    plt.ylabel('max value function')
    plt.title('max value functions over # of iterations')
    plt.show()


def evaluate(board, size):
    val_func = 0
    queue1 = queue.Queue(maxsize=0)
    visited = [['X' for j in range(size)] for i in range(size)]
    node_count = 0
    queue1.put((0, 0, node_count))

    while(queue1.empty() == False):
        pos = queue1.get()
        row, col, node_count = pos
        
        if(visited[row][col] == 'X'):
            visited[row][col] = node_count
            node_count += 1

            if(col + board[row][col] >= 0 and col + board[row][col] < size):
                queue1.put((row, col + board[row][col], node_count))
            if(row + board[row][col] >= 0 and row + board[row][col] < size):
                queue1.put((row + board[row][col], col, node_count))
            if(row - board[row][col] >= 0 and row - board[row][col] < size):
                queue1.put((row - board[row][col], col, node_count))
            if(col - board[row][col] >= 0 and col - board[row][col] < size):
                queue1.put((row, col - board[row][col], node_count))
    if(visited[size-1][size-1] != 'X'):
        val_func = visited[size-1][size-1]
    else:
        for row in visited:
            val_func += row.count('X')
        val_func *= -1

    return (visited, val_func)
        

def pboard(board, size, val_func):
    print('------------------------------------')
    print('Cell Values Board')
    for i in range(size):
        print(board[i])
    print("value function is: ", val_func)



def build_GUI():
    valid_sizes = [5, 7, 9, 11]
    grid_size = 0

    while grid_size not in valid_sizes:
        print('Pick a puzzle grid size: 5, 7, 9, or 11')
        grid_size = int(input())

    print('------------------------------------')

    grid = [[0] * grid_size for i in range(grid_size)]

    for i in range(grid_size):
        for j in range(grid_size):
            if i == grid_size-1 and j == grid_size-1:
                break
            else:
                max_move = max(grid_size - (i+1), i, grid_size - (j+1), j)
                grid[i][j] = randint(1, max_move)

    print('Board')
    for i in range(grid_size):
        print(grid[i])
    
    return (grid, grid_size)

if __name__ == "__main__":
    main()


    # board = [[2, 2, 2, 4, 3],
    # 		[2, 2, 3, 3, 3],
    # 		[3, 3, 2, 3, 3],
    # 		[4, 3, 2, 2, 2],
    # 		[1, 2, 1, 4, 0]]
    # board2 = [[3, 3, 2, 4, 3],
    # 		[2, 2, 2, 1, 1],
    # 		[4, 3, 1, 3, 4],
    # 		[2, 3, 1, 1, 3],
    # 		[1, 1, 3, 2, 0]] 

    # pboard(evaluate(board, 5), 5)
    # pboard(board, 5)
    # pboard(evaluate(board2, 5), 5)
    # pboard(board2, 5)