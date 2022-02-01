def min_domino_rotations(tops: [int], bottoms: [int]) -> int:
	def get_rotations(a: [int], b: [int], target: int) -> int:
		count = 0
		for i in range(len(a)):
			if a[i] == target:
				continue
			if b[i] == target:
				count +=1
			else:
				return float('inf')
		return count

	res = float('inf')
	for i in range(1, 7):
		a = get_rotations(tops, bottoms, i)
		b = get_rotations(bottoms, tops, i)
		res = min(res, a,b)
	return res if res != float('inf') else -1
