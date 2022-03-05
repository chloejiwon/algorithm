def fourSum(nums: [int], target: int) -> [[int]]:
	def threeSum(lo, hi, t: int) -> [[int]]:
		r = []
		for i in range(lo, hi-2):
			start, end = i+1, hi-1
			while start < end:
				s = nums[i]+nums[start]+nums[end]
				if s == t:
					r.append([nums[i], nums[start], nums[end]])
					start += 1
					end -= 1
				elif s < t:
					start += 1
				elif s > t:
					end -= 1
		return r
			
	n = len(nums)
	nums.sort()

	res = []
	for i in range(n-3):
		for l in threeSum(i+1, n, target-nums[i]):
			l.append(nums[i])
			if l not in res:
				res.append(l)
	
	return res


answer = fourSum([1,0,-1,0,-2,2], 0)
print(answer, " == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]")
