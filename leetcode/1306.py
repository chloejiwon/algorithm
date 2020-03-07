# 1306. Jump Game 2
# Solution 1 - BFS
import Queue

class Solution(object):
	def canReach(self,arr,start):
		"""
		:type arr:List[int]
		:type start:int
		:rtype:bool
		"""
		if not arr:
			return False
		N = len(arr)
		q = Queue.Queue()
		q.put(start)
		res = False
		isVisited = [False] * N
		isVisited[start] = True
		while q.empty()==False:
			cur = q.get()
			#print cur
			if arr[cur] == 0:
				res = True
				break
			next = cur+arr[cur]
			if next >=0 and next < N  :
				if isVisited[next]==False:
					q.put(next)
					isVisited[next]=True
			next = cur-arr[cur]
			if next >=0 and next <N:
				if isVisited[next] == False:
					q.put(next)
					isVisited[next]=True
		return res

sol = Solution()
arr = [3,0,2,1,2]
start = 2
print sol.canReach(arr,start)
