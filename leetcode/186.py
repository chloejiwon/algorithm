"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
row <-> column
"""
# Solution 1 
# Brute Force
# : matrix[i][j] ==> matrix[j][N-i]
# : key point in it needs to be done !!!in-place!!!
def rotate(matrix):
	"""
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
	N = len(matrix)
	# transpose
	for i in range(N):
		for j in range(i,N,1):
			matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
	# flip the matrix horizontally
	for i in range(N/2):
		for j in range(N):
			matrix[j][i],matrix[j][N-1-i] = matrix[j][N-1-i],matrix[j][i]
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
rotate(matrix)
print matrix

matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
rotate(matrix)
print matrix
