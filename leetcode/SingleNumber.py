# Single Number - Easy
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""
def singleNumber(nums):
	dic = {}
	for i in nums:
		if dic.get(i):
			dic[i]+=1
		else :
			dic[i]=1
	for i in set(nums):
		if dic[i] == 1:
			return i
	return 0

arr = [2,2,1]
print singleNumber(arr)

arr = [4,1,2,1,2]
print singleNumber(arr)
