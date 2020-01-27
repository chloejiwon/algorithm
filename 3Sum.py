"""
# 3 Sum
Given an array nums of n integers, are there any elements a,b,c in nums
such that a+b+c = 0 ?
Find all unique triplets in the array which gives the sum of zero.

Key is to find *UNIQUE* triplets and make it FASTER!
"""
def threeSum(nums):
	res = []
	nums.sort()
	length = len(nums)
	for i in range(length-2):
		if nums[i] > 0 : break
		if i>0 and nums[i] == nums[i-1] : continue
		l, r = i+1, length-1
		while l<r:
			sum = nums[i] + nums[l] + nums[r]
			if sum < 0 :
				l += 1
			elif sum > 0 :
				r-=1
			else:
				res.append([nums[i],nums[l],nums[r]])
				while l<r and nums[l] == nums[l+1]:
					l+=1
				while l<r and nums[r] == nums[r-1] :
					r-=1
				l+=1
				r-=1
	
	return res
