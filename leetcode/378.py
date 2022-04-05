def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
	n = len(matrix)
	
	left, right = matrix[0][0], matrix[n-1][n-1]
	while left < right:
	    mid = (left+right)//2
	    
	    cnt = 0
	    j = n-1
	    for i in range(n):
	        while j>=0 and matrix[i][j] > mid: 
	            j -= 1
	        cnt += (j+1)
	                
	    if cnt >= k:
	        right = mid
	    else:
	        left = mid+1
	        
	return left


