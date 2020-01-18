class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        direction = [(-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1),(1,-1),(-1,1)]
        newGrid = []
        r = len(M)
        c = len(M[0])
        for i in range(r):
            newGrid.append([])
            for j in range(c):
                # (i,j)
                count = 1
                value = M[i][j]
                for dx,dy in direction:
                    nx = i+dx
                    ny = j+dy
                    if 0<=nx<r and  0<=ny<c :
                        value += M[nx][ny]
                        count+=1
                value  = value / count;
                newGrid[i].append(value)
                
        return newGrid
