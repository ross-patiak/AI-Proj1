import queue
def main():
    board1 = [[3, 2, 1, 4, 1],
            [3, 2, 1, 3, 3],
            [3, 3, 2, 1, 4],
            [3, 1, 2, 3, 3],
            [1, 4, 4, 3, 0]]

    board = [[2, 2, 2, 4, 3],
            [2, 2, 3, 3, 3],
            [3, 3, 2, 3, 3],
            [4, 3, 2, 2, 2],
            [1, 2, 1, 4, 0]]

    visited, value = evaluate(board, 5)
    pboard(visited, 5, value)

    shortest = spf(board, 5)
    print(shortest)


    #general demonstration of build_GUI function AKA task 2

    #general demonstratjion of execution function AKA task 3
   

def pboard(board, size, val_func):
    for i in range(size):
        print(board[i])
    print("value function is: ", val_func)


#general demonstration of Hill Climb function AKA task 4 FOR ALL LEGAL BOARD SIZES


def spf(board, size):
    val_func = 0
    pri_queue = queue.PriorityQueue(maxsize=0)
    visited = [[False] * size for i in range(size)]
    path_length = 0
    pri_queue.put((0, 0, path_length))

    while(pri_queue.empty() == False):
        pos = pri_queue.get()
        row, col, path_length = pos
        #print(path_length)

        if(row == size-1 and col == size-1):
            return path_length
        
        if(visited[row][col] == False):
            visited[row][col] = True
            path_length += 1

            if(col + board[row][col] >= 0 and col + board[row][col] < size):
              # path_length += board[row][col+board[row][col]]
                pri_queue.put((row, col + board[row][col], path_length))
            if(row + board[row][col] >= 0 and row + board[row][col] < size):
               # path_length += board[row+board[row][col]][col]
                pri_queue.put((row + board[row][col], col, path_length))
            if(row - board[row][col] >= 0 and row - board[row][col] < size):
               # path_length += board[row-board[row][col]][col]
                pri_queue.put((row - board[row][col], col, path_length))
            if(col - board[row][col] >= 0 and col - board[row][col] < size):
               # path_length += board[row][col-board[row][col]]
                pri_queue.put((row, col - board[row][col], path_length))


def evaluate(board, size):
    val_func = 0
    queue1 = queue.Queue(maxsize=0)
    visited = [['X'] * size for i in range(size)]
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

if __name__ == "__main__":
    main()