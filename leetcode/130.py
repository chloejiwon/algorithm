def solve(board: [[str]]) -> None:
	m = len(board)
	n = len(board[0])

	preserved = []
	for i in range(m):
		preserved.append([False]*n)

	# find all connected area to the board[i][j]
	def find(r, c) -> None:
		if preserved[r][c]:
			return

		preserved[r][c] = True

		dir = [(-1,0), (1,0), (0,1), (0,-1)]
		for d in dir:
			if r+d[0] >= 0 and r+d[0] < m and c+d[1] >= 0 and c+d[1] <n:
				if board[r+d[0]][c+d[1]] == "O":
					find(r+d[0], c+d[1])
		return

	# first row
	for i in range(0, n):
		if board[0][i] == "O":
			find(0,i)

	# right column
	for i in range(0, m):
		if n-1 >= 0 and board[i][n-1] == "O":
			find(i, n-1)

	# bottom row
	for i in range(0, n):
		if m-1 >= 0 and board[m-1][i] == "O":
			find(m-1, i)

	# left column
	for i in range(0, m):
		if board[i][0] == "O":
			find(i, 0)

	for i in range(0,m):
		for j in range(0,n):
			if preserved[i][j] == False and board[i][j]=='O':
				board[i][j] = 'X'

	return


board=[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

solve(board)


print(board, "\n", "should be")

print([["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]])
