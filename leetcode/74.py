def searchMatrix(matrix: [[int]], target: int) -> bool:
	m, n = len(matrix), len(matrix[0])
	arr = []
	for row in matrix:
		arr += row
	
	def binarySearch() -> bool:
		low, high = 0, m*n-1
		while low <= high:
			mid = (low + high) // 2
			if arr[mid] == target:
				return True
			elif arr[mid] < target:
				low = mid + 1
			else:
				high = mid - 1
		return False

	return binarySearch()

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), "should be True")
