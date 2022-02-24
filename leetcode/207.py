class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i: int) -> bool:
            visited[i] = 1
            if i in graph:
                for j in graph[i]:
                    if visited[j] == 0:
                        if not dfs(j): return False
                    elif visited[j] == 1:
                        return False
            visited[i]=2
            return True
            
            
        graph = {}
        for p in prerequisites:
            if p[0] in graph:
                graph[p[0]].add(p[1])
            else:
                graph[p[0]] = set([p[1]])
        
        visited = [0]*numCourses
        
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i): return False
            
        return True
