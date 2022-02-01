def indexes(nums: [int], target: int) -> int:
	if not nums:
		return [-1, -1]

	def search_num(num):
		lo, hi  = 0, len(nums)
		while lo < hi:
			mid = (lo + hi)//2
			if nums[mid] < num:
				lo = mid+1
			else:
				hi = mid
		return lo

	left = search_num(target)
	right = search_num(target+1) -1
	if left <= right:
		return [left, right]
	else:
		return [-1, -1]
