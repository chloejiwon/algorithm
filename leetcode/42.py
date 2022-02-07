# Solution1: 2 pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        water = 0
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
                
        return water
