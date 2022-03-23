def findMin(nums: [int]) -> int:
	left, right = 0, len(nums)-1
	
	def search(i, j):
		while i < j:
			mid = (i+j) // 2
			if nums[mid] < nums[j]:
				if nums[i] < nums[mid]:
					j = mid-1
				else:
					j = mid
			else:
				if nums[i] <= nums[mid]:
					i = mid+1
				else:
					i = mid
		return nums[i]

	return search(left, right)

print(findMin([3,4,5,1,2]) == 1)
print(findMin([1,2,3,4,5,6]) == 1)
print(findMin([-500,-1000,-700]) == -1000)
