def find_k_pairs_with_smallest_sums(nums1: [int], nums2: [int], k: int) -> [[int]]:
	import heapq
	res = []
	m, n = len(nums1), len(nums2)
	visited = set()
	q = [(nums1[0]+nums2[0], (0,0))]
	for _ in range(min(k, m*n)):
		val, (i,j) = heapq.heappop(q)
		res.append([nums1[i], nums2[j]])
		while i+1 < m and (i+1, j) not in visited:
			heapq.heappush(q, (nums1[i+1]+nums2[j], (i+1,j)))
			visited.add((i+1, j))
		while j+1 < n and (i, j+1) not in visited:
			heapq.heappush(q, (nums1[i]+nums2[j+1], (i,j+1)))
			visited.add((i,j+1))
	return res

print(find_k_pairs_with_smallest_sums([1,7,11], [2,4,6], 3))
print(find_k_pairs_with_smallest_sums([1,1,2], [1,2,3], 2))
