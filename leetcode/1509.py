def minimum_difference(nums: [int]) -> int:
	n = len(nums)
	nums.sort()
	
	if n <= 3:
		return 0
	
	res = float('inf')
	for i in range(0,4):	
		res = min(res, nums[i+(n-3)-1]-nums[i])

	return res

print(minimum_difference([1,5,10,14]))
