def findRadius(houses, heaters):
	houses.sort()
	heaters.sort()

	last_heater = len(heaters)-1
	ans = 0
	left_heater, right_heater = 0, 0
	for house in houses:
		while right_heater < last_heater and house > heaters[right_heater]:
			left_heater, right_heater = right_heater, right_heater+1
		d1, d2 = abs(heaters[left_heater]-house), abs(heaters[right_heater]-house)
		ans = max(ans, min(d1, d2))
	return ans


tc = [([1,2,3],[2]), ([1,2,3,4],[1,4]), ([1,5],[2])]
answers = [1,1,3]

passed = True
for i in range(len(tc)):
	t = tc[i]
	if answers[i] != findRadius(t[0], t[1]):
		passed = False

print(passed)	
