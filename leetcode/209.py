def minimumSubarray(nums: [int], target: int) -> int:
	left = 0
	sumSubArray = 0
	res = float('inf')
	for right, num in enumerate(nums):
	    sumSubArray += num
	    while sumSubArray >= target:
	        res = min(res, right-left+1)
	        sumSubArray -= nums[left]
	        left += 1
	        
	if res == float('inf'):
	    return 0
	
	return res


print(minimumSubarray([2,3,1,2,4,3],7), "should be 2")
