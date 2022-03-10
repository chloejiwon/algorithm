def binary_subarrays_with_sum(nums: [int], goal: int) -> int:
	def at_most(k):
		if k < 0: return 0
		tmp = res = i = 0
		for j in range(len(nums)):
			tmp += nums[j]
			while tmp > k:
				tmp -= nums[i]
				i += 1
			res += j - i + 1 
		return res
	return at_most(goal) - at_most(goal-1)

print(binary_subarrays_with_sum([1,0,1,0,1], 2))
print(binary_subarrays_with_sum([0,0,0,0,0], 0))
print(binary_subarrays_with_sum([1,1,1,1,1], 1))
