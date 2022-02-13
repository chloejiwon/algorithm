def container_water(height: [int]) -> int:
	left, right = 0, len(height)-1
	water = 0
	
	while left < right:
		if height[left] < height[right]:
			if water < (right-left) * height[left]:
				water = (right-left) * height[left]
			left += 1
		else:
			if water < (right-left) * height[right]:
				water = (right-left) * height[right]
			right -= 1
			
	return water


print(container_water([1,8,6,2,5,4,8,3,7]))
