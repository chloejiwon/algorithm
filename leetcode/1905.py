def count_sub_islands(grid1: [[int]], grid2: [[int]]) -> int:
	res = 0
	row, col = len(grid2), len(grid2[0])
	def visit_bfs(r: int, c: int) -> bool:
	    sub_islands = True
	    
	    # visit
	    grid2[r][c] = 0
	    if grid1[r][c] == 0:
	        sub_islands = False
	        
	    dir = [(0,1), (1,0), (0, -1), (-1, 0)]
	    for move in dir:
	        next_r, next_c = r+move[0], c+move[1]
	        if next_r < row and next_c < col and next_r >= 0 and next_c >= 0:
	            if grid2[next_r][next_c] == 1:
	                if visit_bfs(next_r, next_c) == False:
	                    sub_islands = False
	
	    return sub_islands
	
	for r in range(row):
	    for c in range(col):
	        # find the starting position
	        if grid2[r][c] == 1:
	            if visit_bfs(r,c) == True:
	                res += 1
	
	return res


print(count_sub_islands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]) == 3)
print(count_sub_islands([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]) == 2)
