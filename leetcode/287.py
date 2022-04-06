def find_duplicate(nums: [int]) -> int:
	left, right = 0, len(nums)-1
	duplicate = 0
	while left <= right:
		mid = (left+right)//2
		
		count = sum(num<=mid for num in nums)
		if count > mid:
			duplicate = mid
			right = mid - 1
		else:
			left = mid + 1

	return duplicate
