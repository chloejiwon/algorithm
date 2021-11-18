# 200. Number of islands

#Solution 1 Using Stack - Wrong answer
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        N = len(grid)
        M = len(grid[0])
        if N==0 :
                return 0
        dirr = [[0,1],[1,0],[-1,0],[0,-1]]
        count = 0
        land = 0
	stack = []
        for i in range(N):
            for j in range(M):
                if grid[i][j]=='1':
                    stack.append([i,j])
                    land+=1
        cnt = 0
        while len(stack)==0:
                loc = stack.pop()
                if grid[loc[0]][loc[1]] == '1':
                    grid[loc[0]][loc[1]] = '3'
                    cnt+=1
                    isIsland = True
                    for i in range(4):
                            nx,ny = loc[0]+dirr[i][0],loc[1]+dirr[i][1]
                            if nx >=0 and nx<N and ny >=0 and ny<M:
                                    if grid[nx][ny]=='1':
                                        stack.append([nx,ny])
                                        isIsland = False
                    if isIsland==True:
                        count+=1
        return count

# Solution 2 - Using stack for start point & Queue : Time Limit Exceeded

import Queue
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        N = len(grid)
        M = len(grid[0])
        if N==0 :
                return 0
        dirr = [[0,1],[1,0],[-1,0],[0,-1]]
        count = 0
        land = 0
        stack,q=[],Queue.Queue()
        for i in range(N):
            for j in range(M):
                if grid[i][j]=='1':
                    stack.append([i,j])
                    land+=1
        cnt = 0
        while len(stack)!=0:
                loc = stack.pop() # starting Point
                if grid[loc[0]][loc[1]] == '1':
                    q.put([loc[0],loc[1]])
                    cnt+=1
                    while q.empty()==False:
                        adj = q.get()
                        grid[adj[0]][adj[1]]='3'
                        for i in range(4):
                                nx,ny = adj[0]+dirr[i][0],adj[1]+dirr[i][1]
                                if nx >=0 and nx<N and ny >=0 and ny<M:
                                        if grid[nx][ny]=='1':
                                            q.put([nx,ny])
                                            isIsland = False
                    count+=1
        return count


# Solution 3 - Stack for starting point & Queue for searching
# Only Beat 5.16%, But pass;;
import Queue
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        N = len(grid)
        M = len(grid[0])
        if N==0 :
                return 0
        dirr = [[0,1],[1,0],[-1,0],[0,-1]]
        count = 0
        land = 0
        stack,q=[],Queue.Queue()
        for i in range(N):
            for j in range(M):
                if grid[i][j]=='1':
                    stack.append([i,j])
                    land+=1
        cnt = 0
        while cnt!=land:
                loc = stack.pop() # starting Point
                if grid[loc[0]][loc[1]] == '1':
                    q.put([loc[0],loc[1]])
                    while q.empty()==False:
                        adj = q.get()
                        if grid[adj[0]][adj[1]]=='1':
                            grid[adj[0]][adj[1]]='3'
                            cnt+=1
                            for i in range(4):
                                    nx,ny = adj[0]+dirr[i][0],adj[1]+dirr[i][1]
                                    if nx >=0 and nx<N and ny >=0 and ny<M:
                                            if grid[nx][ny]=='1':
                                                q.put([nx,ny])
                    count+=1
        return count


# Solution 4 - hmm.... I thought it would make time less...but just a little
import Queue
class Solution(object):
    def bfs(self,grid,N,M,x,y):
        dirr = [[0,1],[1,0],[-1,0],[0,-1]]
        q = Queue.Queue()
        if grid[x][y] == '1':
            q.put([x,y])
            while q.empty()==False:
                adj = q.get()
                if grid[adj[0]][adj[1]]=='1':
                    grid[adj[0]][adj[1]]='3'
                    for i in range(4):
                            nx,ny = adj[0]+dirr[i][0],adj[1]+dirr[i][1]
                            if nx >=0 and nx<N and ny >=0 and ny<M:
                                    if grid[nx][ny]=='1':
                                        q.put([nx,ny])
        return grid
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        N = len(grid)
        M = len(grid[0])
        if N==0 :
                return 0
        count = 0
        land = 0
        stack,q=[],Queue.Queue()
        for i in range(N):
            for j in range(M):
                if grid[i][j]=='1':
                    stack.append([i,j])
                    grid = self.bfs(grid,N,M,i,j)
                    count+=1
        return count




# Solution 5
class Solution(object):
    # BFS
    def visitIslands(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return
        if grid[r][c] == "0":
            return
        
        # visit
        grid[r][c] = "0"
        self.visitIslands(grid, r-1, c)
        self.visitIslands(grid, r, c-1)
        self.visitIslands(grid, r+1, c)
        self.visitIslands(grid, r, c+1)
        return
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        num = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    self.visitIslands(grid, i, j)
                    num += 1
                    
        return num
        
