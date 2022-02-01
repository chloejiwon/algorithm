def min_domino_rotations(tops: [int], bottoms: [int]) -> int:
	a, b, c, d = 0, 0, 1, 1
	# 1. count swaps based on tops[0]
	# 2. count swaps based on bottoms[0]
	for i in range(1, len(tops)):
		# check 'a'
		if bottoms[i] == tops[0] and bottoms[i]!=tops[i]:
			if a != -1: a+=1
		else bottoms[i] != tops[0] and tops[i] != tops[0]:
			a=-1
		# check 'b'
		if tops[i] == bottoms[0] and bottoms[i]!=tops[i]:
			if b != -1: b+=1
		else tops[i] != bottoms[0] and bottoms[i] != bottoms[0]:
			b = -1
		# check 'c'
		if bottoms[i] == bottoms[0] and bottoms[i]!=tops[i]:
			if c != -1: c+=1
		else bottoms[i] != bottoms[0] and tops[i] != bottoms[0]:
			c=-1
		# check 'd'
		if tops[i] == tops[0] and bottoms[i]!=tops[i]:
			if d != -1: d+=1
		else tops[i] != tops[0] and bottoms[i] != tops[0]:
			d = -1
	
	# 3. return minimum counts 
	res = -1
	for t in [a,b,c,d]:
		if t == -1:
			continue
		if res == -1: res = t
		else: res = min(res,t)

	return res
