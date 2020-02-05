"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
row <-> column
"""
# Solution 1 
# Brute Force
# idx change. matrix[0][0] ==> matrix[0][N]
# 	      matrix[N][N] ==> matrix[N][0]
#	      matrix[N][0] ==> matrix[0][N]
#	      matrix[i][j] ==> matrix[(i+N/2)][]
def rotate(matrix):
	"""
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
	N = len(matrix)	
	for i in range(N):
		col = []
		for j in range(N):
			col.append( matrix[j][i])
		
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
rotate(matrix)
print matrix
