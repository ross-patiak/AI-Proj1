import os
import sys
import queue
def main():
	board = [[2, 2, 2, 4, 3],
			[2, 2, 3, 3, 3],
			[3, 3, 2, 3, 3],
			[4, 3, 2, 2, 2],
			[1, 2, 1, 4, 0]]
	board2 = [[3, 3, 2, 4, 3],
			[2, 2, 2, 1, 1],
			[4, 3, 1, 3, 4],
			[2, 3, 1, 1, 3],
			[1, 1, 3, 2, 0]] 
#	print(board[2][0])
#	print(board[0][2])
	pboard(evaluate(board, 5), 5)
	pboard(board, 5)
	pboard(evaluate(board2, 5), 5)
	pboard(board2, 5)

def evaluate(board, size):
	val_func = 0
	queue1 = queue.Queue(maxsize=0)
	visited = [['X' for j in range(size)] for i in range(size)]
	node_count = 0
	queue1.put((0, 0, node_count))
	#count=0
	while(queue1.empty() == False):
		pos = queue1.get()
		row, col, node_count = pos
		print(row,col)
		#if(node_count == 7):#row == size-1 and col == size-1):
		#	return visited
		if(visited[row][col] == 'X'):
			visited[row][col] = node_count
			node_count += 1
			#print(row)
			if(col + board[row][col] >= 0 and col + board[row][col] < size):
				print('1st')
				#print(col + board[row][col])
				queue1.put((row, col + board[row][col], node_count))
			if(row + board[row][col] >= 0 and row + board[row][col] < size):
				print('2nd')
				#print(row + board[row][col])
				queue1.put((row + board[row][col], col, node_count))
			if(row - board[row][col] >= 0 and row - board[row][col] < size):
				print('3rd')
				#print(row - board[row][col])
				queue1.put((row - board[row][col], col, node_count))
			if(col - board[row][col] >= 0 and col - board[row][col] < size):
				print('4th')
				#print(col - board[row][col])
				queue1.put((row, col - board[row][col], node_count))
	if(visited[size-1][size-1] != 'X'):
		val_func = visited[size-1][size-1]
	else:
		for row in visited:
			val_func += row.count('X')
		val_func *= -1
	print("value function is: ", val_func)
	
	return visited
		#count+=1
		#print("loop count:" + str(count))







def pboard(board, size):
	for i in range(size):
		print(board[i])

if __name__ == "__main__":
	main()
