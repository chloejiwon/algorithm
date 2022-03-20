import collections
def smallest_range(nums: [[int]]) -> [int]:
	# Prepare total_arr merged by all nums
	total_arr = {}
	for k, num in enumerate(nums):
	    for a in num:
	        if a in total_arr: total_arr[a].append(k)
	        else: total_arr[a] = [k]
	total_arr = sorted(total_arr.items())
	total_len = len(total_arr)
	
	min_dist, res = float('inf'), []
	counter = collections.Counter()
	start, end = 0, 0
	counter_size = 0

	nums_len = len(nums)
	while end < len(total_arr):
		# Count 
		for k in total_arr[end][1]:
				counter[k] += 1
				if counter[k] == 1: counter_size += 1

		# Check if [start:end] meets the condition
		while counter_size == nums_len:
			# Process the condition and update results
			if min_dist > (total_arr[end][0]-total_arr[start][0]):
				min_dist = total_arr[end][0]-total_arr[start][0]
				res = [total_arr[start][0], total_arr[end][0]]
			
			# Contract the window
			for k in total_arr[start][1]:
					counter[k] -= 1
					if counter[k] == 0: counter_size -= 1
			start += 1

		# Update end
		end += 1
		

	return res


print(smallest_range([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
print(smallest_range([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]) == [20,24])
print(smallest_range([[1,2,3],[1,2,3],[1,2,3]]))
print(smallest_range([[1,2,3],[1,2,3],[1,2,3]]) == [1,1])
