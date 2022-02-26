# Time Complexity: O(n)
# Space Complexity: O(1)
# Algorithm: Sliding Window

def maxLengthSubArray(nums1: [int], nums2: [int]) -> int:
	nums1 = "".join([chr(ch) for ch in nums1])
	res = 0
	temp = ""
	for ch in nums2:
		temp += chr(ch)
		if temp in nums1:
			res = max(res, len(temp))
		else:
			temp = temp[1:]
	return res
