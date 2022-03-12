def nextPermutation(nums: [int]) -> None:
	start = -1
	while start < len(nums):
	    if nums[start+1:] == sorted(nums[start+1:], reverse=True):
	        # nums[start] should be changed with the bigger, smallest element
	        if start == -1:
	            nums.sort()
	            return
	        
	        target, idx = float('inf'), start
	        
	        for j in range(start+1, len(nums)):
	            if nums[start] < nums[j] and target >= nums[j]:
	                target = nums[j]
	                idx = j
	                
	        nums[start], nums[idx] = nums[idx], nums[start]
	        
	        nums[start+1:] = sorted(nums[start+1:])
	        return
	        
	    start += 1
	return

tc = [ [1,2,3], [1,3,4,2] ]
ans = [ [1,3,2], [1,4,2,3] ]

for i, t in enumerate(tc):
	nextPermutation(t)
	print(t == ans[i])

