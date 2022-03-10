def max_consecutive_ones(nums: [int], k: int) -> int:
	res = 0

	i = 0
	c = 0
	for j, num in enumerate(nums):
		if num == 0:
			c += 1
		while c > k:
			if nums[i] == 0:
				c -= 1
			i += 1
		res = max(res, j-i+1)

	return res


print(max_consecutive_ones([1,1,1,0,0,0,1,1,1,1,0], 2))
print(max_consecutive_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
