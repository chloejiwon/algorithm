def find_kth_smallest_distance(nums: [int], k: int) -> int:
	nums.sort()
	
	def is_there_k_distances_less_than(guess: int) -> bool:
		i = count = 0
		j = 1

		while i < len(nums):
			while j < len(nums) and (nums[j] - nums[i]) <= guess:
				j += 1
			count += j-i-1
			i += 1

		return count >= k

	left, right = 0, nums[-1]-nums[0]
	while left < right:
		mid = (left + right) // 2
		if is_there_k_distances_less_than(mid):
			right = mid
		else:
			left = mid+1

	return left

print(find_kth_smallest_distance([1,1,1],2))
print(find_kth_smallest_distance([1,3,1],1))
print(find_kth_smallest_distance([1,6,1],3))
