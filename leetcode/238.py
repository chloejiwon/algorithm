def product_except_self(nums: [int]) -> [int]:
	prod, prod_nonzero, zero_cnt = 1, 1, 0
	for num in nums:
		prod *= num
		if num != 0:
			prod_nonzero *= num
		else:
			zero_cnt += 1

	res = []
	for num in nums:
		if num != 0:
			res.append(prod//num)
		else:
			if zero_cnt == 1:
				res.append(prod_nonzero)
			else:
				res.append(0)
	return res


print(product_except_self([1,2,3,4]))
print(product_except_self([-1,1,0,-3,3]))
