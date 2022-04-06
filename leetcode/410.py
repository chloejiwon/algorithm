def split_arrays_largest_sum(nums: [int], m: int) -> int:

	def split_arrays(subarray_sum: int) -> int:
		current_sum = 0
		splits_required = 0

		for num in nums:
			if current_sum + num <= subarray_sum:
				current_sum += num
			else:
				current_sum = num
				splits_required += 1

		return splits_required + 1

	res = 0
	left, right = max(nums), sum(nums)
	while left <= right:
		mid = (left + right) // 2
		
		if split_arrays(mid) <= m:
			right = mid - 1
			res = mid
		else:
			left = mid + 1
	return res

print(split_arrays_largest_sum([7,2,5,6,8,4,3], 3), " should be 14")
