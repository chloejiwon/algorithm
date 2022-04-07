import collections

def number_of_good_ways(s: str) -> int:
	res = 0
	right_side_map = collections.Counter(s)
	left_side_map = {}
	left_side_distinct_number = 0
	right_side_distinct_number = len(right_side_map)

	for i in range(1, len(s)):
		if s[i-1] not in left_side_map:
			left_side_map[s[i-1]]=1
			left_side_distinct_number += 1
		right_side_map[s[i-1]] -= 1
		if right_side_map[s[i-1]] == 0:
			right_side_distinct_number -= 1

		if left_side_distinct_number == right_side_distinct_number:
			res += 1
	return res

print(number_of_good_ways("aacaba"), " should be 2")

