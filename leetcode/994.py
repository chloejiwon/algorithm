# 994. Rotting Oranges

# Solution 1  - Using BFS, Beating 14.93%
import Queue

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
                return -1
        q = Queue.Queue()
        N,M = len(grid), len(grid[0])
        minutes,totalOrange = 0,0

        for i in range(N):
                for j in range(M):
                        if grid[i][j]==2:
                                q.put([i,j])
                        elif grid[i][j]==1:
                                totalOrange+=1
        cnt = 0
        dirr = [[0,1],[0,-1],[1,0],[-1,0]]
        while cnt < totalOrange :
                thisTime = q.qsize()
                if thisTime >0 :
                    minutes+=1
                elif thisTime == 0 :
                    break
                for i in range(thisTime):
                    cur = q.get()
                    if grid[cur[0]][cur[1]] == 2:
                            grid[cur[0]][cur[1]] =3
                            for i in range(4):
                                    nx,ny = cur[0]+dirr[i][0],cur[1]+dirr[i][1]
                                    if nx >=0 and nx <N and ny >=0 and ny <M :
                                            if grid[nx][ny]==1:
                                                    q.put([nx,ny])
                                                    cnt+=1     
                                                    grid[nx][ny]=2

        if cnt != totalOrange:
                return -1
        else:
                return minutes

