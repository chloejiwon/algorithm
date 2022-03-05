def threeSumClosest(nums: [int], target: int) -> int:
	n = len(nums)
	nums.sort()
	
	minDist = float('inf')
	res = float('inf')
	for i in range(0, n-2):
	    start, end = i+1, n-1
	    while start < end:
	        tmp = target - (nums[i]+nums[start]+nums[end])
	        if abs(tmp) < minDist:
	            res = nums[i]+nums[start]+nums[end]
	            minDist = abs(tmp)
	        if tmp > 0:
	            start += 1
	        elif tmp < 0:
	            end -= 1
	        else:
	            return target
	return res

print(threeSumClosest([-1,2,1,-4], 1), "should be 2")
