class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        
        x, y = len(nums1), len(nums2)
        if x > y:
            nums1, nums2 = nums2, nums1
            x, y = y, x
        start, end = 0, x
        
        while start <= end:
            partitionX = (start + end) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            
            maxLeftX, minRightX = -1000001, 1000001
            if partitionX > 0:
                maxLeftX  = nums1[partitionX-1]
            if partitionX < x:
                minRightX = nums1[partitionX]
            
            maxLeftY, minRightY = -1000001, 1000001
            if partitionY > 0:
                maxLeftY  = nums2[partitionY-1]
            if partitionY < y:
                minRightY = nums2[partitionY]
            
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x+y)%2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                end = partitionX - 1
            else:
                start = partitionX + 1
        
        return 0.0
