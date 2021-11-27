class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        l, r = grid[0][0], N*N-1
        def reachable(t):
            bfs = [(0,0)]
            seen = set((0,0))
            for x, y in bfs:
                if grid[x][y] <= t:
                    if x == y == N-1: return True
                    else:
                        adj = [(0,1), (1,0), (-1,0), (0,-1)]
                        for i,j in adj:
                            if 0<=x+i<N and 0<=y+j<N and (x+i, y+j)  not in seen:
                                bfs.append((x+i, y+j))
                                seen.add((x+i, y+j))
            return False
        while l < r:
            m = (l+r)/2
            if reachable(m): r=m
            else: l = m+1
        return l
