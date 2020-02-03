# Two Sum
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
def twoSum(nums, target):
	res = []
	for idx,num in enumerate(nums):
		for j in range(idx+1,len(nums),1):
			if num + nums[j] == target:
				res.append(idx)
				res.append(j)

	return res

nums  = [2,7,11,15]
target = 9
print twoSum(nums,target)
