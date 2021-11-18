class Solution(object):
	def twoSum(self, nums, target):
		answer = []
		indexes = {}
		for i in range(len(nums)):
			diff = target - nums[i]
			if diff in indexes:
				answer.append(indexes[diff])
				answer.append(i)
			else:
				indexes[nums[i]]=i
		return answer

sol = Solution()
testcases = [([2,7,11,15], 9), ([3,2,4],6), ([3,3],6)]
answers = [[0,1], [1,2], [0,1]]

success = True
for i in range(len(testcases)):
	tc = testcases[i]
	if answers[i] != sol.twoSum(tc[0], tc[1]):
		success = False


if success:
	print("Passed!")
else:
	print("Failed!")
